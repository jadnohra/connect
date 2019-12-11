#!/usr/bin/python3

import yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)

db = yaml.load(open('./data/esu-ma-735.yaml'))
pp.pprint(db)
