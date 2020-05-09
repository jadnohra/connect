from ddq.topics.set_theory.topic import topic
from ddq.util.print_tree import print_node


ST = topic()
print_node(ST.get_axioms()[0].get_formula())