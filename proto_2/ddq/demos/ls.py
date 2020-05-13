import sys
import json
import logging
from types import SimpleNamespace
from pprint import pprint
from ddq.node import Node
from ddq.inductor import Inductor
from ddq.fol.topic import FOL
from ddq.topics.set_theory.topic import ST
from ddq.util.print_tree import print_node


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
        if isinstance(thing, Inductor):
            logging.error("'{}' is an inductor, make sure to provide"
                          " an induction index e.g ST.InductiveFormation(3)\n"
                          .format(sys.argv[1]))
        logging.exception(str(e))
else:
    pprint(list(topics.keys()))
