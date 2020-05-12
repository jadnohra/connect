import sys
import json
from pprint import pprint
from ddq.node import Node
from ddq.util.print_tree import print_node
from ddq.fol.topic import FOL
from ddq.topics.set_theory.topic import ST

topics = {
    "FOL": FOL,
    "ST": ST
}

print_help = True

if len(sys.argv) > 1:
    query = sys.argv[1].split('.')
    if len(query) == 1:
        topic_key = query[0]
        if topic_key in topics:
            pprint(vars(topics[topic_key]))
            print_help = False
    else:
        topic_key = query[0]
        if topic_key in topics:
            topic = topics[topic_key]
            thing_key = query[1]
            if thing_key in vars(topic):
                thing = vars(topic)[thing_key]
                if thing is not None:
                    if not isinstance(thing, Node):
                        thing = thing()
                    print_node(thing)
                    print_help = False

if print_help:
    pprint(list(topics.keys()))