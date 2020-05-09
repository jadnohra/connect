from ddq.util.print_tree import print_node
from ddq.topics.set_theory.topic import topic
from ddq.topics.set_theory.empty_set import EmptySetAxiom

ST = topic()
print_node(ST.find_axiom(EmptySetAxiom).get_formula())
