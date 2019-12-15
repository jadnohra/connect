#!/usr/bin/env python

import argparse
import os
import sys
import yaml
from tabulate import tabulate
import nltk

from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)
k_nltk_stopwords = set(stopwords.words('english'))

parser = argparse.ArgumentParser(description='Query the connect .yaml file')
parser.add_argument("query", help="The search query [key]:[value]", nargs='?', default=None)
parser.add_argument('--file', help='The connect .yaml file')
parser.add_argument('--dump', help='Dump the database', action='store_true')
parser.add_argument('--stats', help='Print database statistics', action='store_true')
parser.add_argument('--dbg_matches', help='Debug individual query matches', action='store_true')

args = parser.parse_args()

data_source = args.file if args.file else './data/.'
db = {}
if os.path.isfile(data_source):
    db = yaml.load(open(data_source), Loader=yaml.FullLoader)
else:
    for root, dirs, files in os.walk(data_source, topdown=True):
        for file in [x for x in files if x.lower().endswith('.yaml')]:
            file_db = yaml.load(open(os.path.join(root, file)), Loader=yaml.FullLoader)
            # TODO prefix keys with filename
            db = {**db , **file_db}

if args.dump:
    print(yaml.dump(db))
if args.stats:
    print("Fact count: {}".format(len(db.keys())))

def recurse_gather(node, search_key, search_value, key='', path='', title=''):
    def soft_match(text, search):
        words = [x.strip().lower() for x in text.split() if len(x.strip())]
        words = [x for x in words if x not in k_nltk_stopwords and len(x) > 1]
        for word in words:
            for item in search:
                if word in item or item in word:
                    if args.dbg_matches:
                        print("match:", text, search, item, word)
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
        if (search_key == '' or (path != '' and soft_match(path, search_key))) and \
            (search_value == '' or soft_match(node, search_value)):
            gathered.append([title, path, node])
    return gathered

def consolidate_gathered(gathered):
    last_title = ''
    for row in gathered:
        if last_title and row[0] == last_title:
            row[0] = ''
        else:
            last_title = row[0]
            if row[0] == '':
                row[0] = '-'

if args.query:
    query = args.query
    key,value = query.split(':')
    gathered = recurse_gather(db, [key.strip().lower()], [value.strip().lower()])
    consolidate_gathered(gathered)
    print(tabulate(gathered, showindex=True))
