import os
import argparse
import yaml
from tabulate import tabulate
from core.core import (
    load_db, pattern_to_keys, recurse_gather, consolidate_gathered)


parser = argparse.ArgumentParser(description='Query the connect .yaml file')
parser.add_argument("query", help="The search query [key]:[value]", nargs='?', default=None)
parser.add_argument('--file', help='The connect .yaml file')
parser.add_argument('--dump', help='Dump the database', action='store_true')
parser.add_argument('--stats', help='Print database statistics', action='store_true')
parser.add_argument('--dbg_matches', help='Debug individual query matches', action='store_true')
parser.add_argument('-mc', '--max_col_width', help='Sets the maximum width of the output table columns', type=int, default=80)
parser.add_argument('--no_nltk', help='Disable nltk', action='store_true')

args = parser.parse_args()

data_source = args.file if args.file else './data/math/.'
db = load_db(data_source)

if args.dump:
    print(yaml.dump(db))
if args.stats:
    print("Fact count: {}".format(len(db.keys())))

tty_rows, tty_cols = [int(x) for x in os.popen('stty size', 'r').read().split()]

if args.query:
    query = args.query
    key,value = query.split(':')
    gathered = recurse_gather(db, pattern_to_keys(key), pattern_to_keys(value))
    consolidate_gathered(gathered, limit_field_width=tty_cols)
    print(tabulate(gathered, showindex=True))
