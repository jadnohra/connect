#!/usr/bin/python3

import argparse
import yaml
import pprint
from collections.abc import Iterable

pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser(description='Query the connect .yaml file')
parser.add_argument('--file', help='The connect .yaml file')
parser.add_argument("query", help="The search query [key]:[value]", default=None)
args = parser.parse_args()

db = yaml.load(open(args.file if args.file else './data/esu-ma-735.yaml'), Loader=yaml.FullLoader)
pp.pprint(db)

def recurse_gather(node, key, value, path=''):
    gathered = []
    for key, item in node.items():
        if isinstance(item, dict):
            gathered.extend(recurse_gather(item, key, value, '{}.{}'.format(path, key)))
        else:
            if (key == '' or node in key) or \
                (value == '' or item in value):
                gathered.append('{}.{}:{}'.format(path, key, value))
    return gathered

query = args.query
key,value = query.split(':')

print(key, value)
pp.pprint(recurse_gather(db, key, value))
