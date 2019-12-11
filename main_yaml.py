#!/usr/bin/python3

import argparse
import yaml
from tabulate import tabulate

parser = argparse.ArgumentParser(description='Query the connect .yaml file')
parser.add_argument("query", help="The search query [key]:[value]", nargs='?', default=None)
parser.add_argument('--file', help='The connect .yaml file')
parser.add_argument('--dump', help='Dump the .yaml file', action='store_true')

args = parser.parse_args()

db = yaml.load(open(args.file if args.file else './data/esu-ma-735.yaml'), Loader=yaml.FullLoader)

if args.dump:
    print(yaml.dump(db))

def recurse_gather(node, search_key, search_value, key='', path='', title=''):
    def soft_match(text, search):
        words = [x.lower() for x in text.split()]
        for word in words:
            for item in search:
                if word in item or item in word:
                    return True
        return False
    gathered = []
    if isinstance(node, dict):
        node_title = node.get('title', '')
        for key, item in node.items():
            if key != 'title':
                gathered.extend(recurse_gather(item, search_key, search_value,
                                key=key, path='{}.{}'.format(path, key),
                                title=node_title))
    elif isinstance(node, list):
        for item in node:
            gathered.extend(recurse_gather(item, search_key, search_value,
                            key='', path=path))
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

if args.query:
    query = args.query
    key,value = query.split(':')
    gathered = recurse_gather(db, [key.lower()], [value.lower()])
    consolidate_gathered(gathered)
    print(tabulate(gathered, showindex=True))
