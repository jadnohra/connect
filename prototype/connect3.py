#!/usr/bin/env python

import argparse
import os
import sys
import yaml
from tabulate import tabulate
import nltk

parser = argparse.ArgumentParser(description='Query the connect .yaml file')
parser.add_argument("query", help="The search query [key]:[value]", nargs='?', default=None)
parser.add_argument('--file', help='The connect .yaml file')
parser.add_argument('--dump', help='Dump the database', action='store_true')
parser.add_argument('--stats', help='Print database statistics', action='store_true')
parser.add_argument('--dbg_matches', help='Debug individual query matches', action='store_true')
parser.add_argument('-mc', '--max_col_width', help='Sets the maximum width of the output table columns', type=int, default=80)
parser.add_argument('--no_nltk', help='Disable nltk', action='store_true')
# TODO use `tput cols` to autodetect a good max_col_width

args = parser.parse_args()

if not args.no_nltk:
    from nltk.corpus import stopwords
    nltk.download('stopwords', quiet=True)
    k_nltk_stopwords = set(stopwords.words('english'))
else:
    k_nltk_stopwords = set()


tty_rows, tty_cols = [int(x) for x in os.popen('stty size', 'r').read().split()]


data_source = args.file if args.file else './data/math/.'
db = {}
if os.path.isfile(data_source):
    db = yaml.load(open(data_source), Loader=yaml.FullLoader)
else:
    for root, dirs, files in os.walk(data_source, topdown=True):
        for file in [x for x in files if x.lower().endswith('.yaml')]:
            file_db = yaml.load(open(os.path.join(root, file)), Loader=yaml.FullLoader)
            if file_db is not None:
                # TODO prefix keys with filename
                db = {**db , **file_db}

if args.dump:
    print(yaml.dump(db))
if args.stats:
    print("Fact count: {}".format(len(db.keys())))

def recurse_gather(node, search_key, search_value, key='', path='', title=''):
    def soft_match(text, search_keys):
        words = [x.strip().lower() for x in text.split() if len(x.strip())]
        words = [x for x in words if x not in k_nltk_stopwords and len(x) > 1]
        for word in words:
            for item in search_keys:
                if word in item or item in word:
                    if args.dbg_matches:
                        print("match:", text, search_keys, item, word)
                    return True
        return False
    gathered = []
    if isinstance(node, dict):
        node_title = node.get('title', title)
        for key, item in node.items():
            if key != 'title':
                gathered.extend(recurse_gather(item, search_key, search_value,
                                key=key, path='{}.{}'.format(path, key),
                                title=node_title))
    elif isinstance(node, list):
        for item in node:
            gathered.extend(recurse_gather(item, search_key, search_value,
                            key='', path=path, title=title))
    else:
        if (len(search_key) == 0 or (path != '' and soft_match(path, search_key))) and \
            (len(search_value) == 0 or soft_match(node, search_value)):
            gathered.append([title, path, node])
    return gathered

def consolidate_gathered(gathered, limit_field_width=80):
    cw_unit = (limit_field_width - 4 - 6) / 6.0
    col_max_widths = [int(1.5*cw_unit), int(1.5*cw_unit), int(2*cw_unit)]
    last_title = ''
    if limit_field_width is not None:
        for row in gathered:
            for i, col in enumerate(row):
                if len(col) > col_max_widths[i]:
                    hw = int(col_max_widths[i] / 2)
                    row[i] = col[:hw-5] + ' ... ' + col[len(col)-(hw+5):]
    for row in gathered:
        if last_title and row[0] == last_title:
            row[0] = ''
        else:
            last_title = row[0]
            if row[0] == '':
                row[0] = '-'

def pattern_to_keys(pattern):
    parts = pattern.split(',')
    return [x.strip().lower() for x in parts if len(x.strip()) > 0]

if args.query:
    query = args.query
    key,value = query.split(':')
    gathered = recurse_gather(db, pattern_to_keys(key), pattern_to_keys(value))
    consolidate_gathered(gathered, limit_field_width=tty_cols)
    print(tabulate(gathered, showindex=True))
