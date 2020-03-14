#!/usr/bin/env python

import os
import sys
import yaml


if '--no_nltk' in sys.argv:
    NLTK_STOPWORDS = set()
else:
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords', quiet=True)
    NLTK_STOPWORDS = set(stopwords.words('english'))


def load_db(file_or_dir: str):
    db = {}
    if os.path.isfile(file_or_dir):
        db = yaml.load(open(file_or_dir), Loader=yaml.FullLoader)
    else:
        for root, dirs, files in os.walk(file_or_dir, topdown=True):
            for file in [x for x in files if x.lower().endswith('.yaml')]:
                file_db = yaml.load(open(os.path.join(root, file)), Loader=yaml.FullLoader)
                if file_db is not None:
                    # TODO prefix keys with filename
                    db = {**db , **file_db}
    return db


def recurse_gather(node, search_key, search_value, key='', path='', title=''):
    def soft_match(text, search_keys):
        words = [x.strip().lower() for x in text.split() if len(x.strip())]
        words = [x for x in words if x not in NLTK_STOPWORDS and len(x) > 1]
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
