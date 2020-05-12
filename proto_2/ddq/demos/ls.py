import sys
import json
import logging
from types import SimpleNamespace
from pprint import pprint
from ddq.node import Node
from ddq.util.print_tree import print_node
from ddq.fol.topic import FOL
from ddq.topics.set_theory.topic import ST

topics = {
    "FOL": FOL,
    "ST": ST
}

if len(sys.argv) > 1:
    try:
        thing = eval(sys.argv[1], topics)
        if isinstance(thing, SimpleNamespace):
            pprint(vars(thing))
        else:
            if not isinstance(thing, Node):
                thing = thing()
            print_node(thing)
    except Exception as e:
        logging.error(str(e))
else:
    pprint(list(topics.keys()))
