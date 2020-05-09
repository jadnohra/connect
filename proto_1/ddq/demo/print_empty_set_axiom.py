from ddq.util.print_tree import print_node
from ddq.util.find_in_list import find_instance_of
from ddq.topics.set_theory.topic import topic
from ddq.topics.set_theory.empty_set import EmptySetAxiom

ST = topic()
axiom = find_instance_of(ST.get_axioms(), EmptySetAxiom)
print_node(axiom.get_formula())
