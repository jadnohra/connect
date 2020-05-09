from ddq.util.print_tree import print_node
from ddq.util.find_in_list import find_instance_of
from ddq.topics.set_theory.topic import topic
from ddq.topics.set_theory.non_membership import NonMembeshipDefinition

ST = topic()
definition = find_instance_of(ST.get_definitions(), NonMembeshipDefinition)
print_node(definition.get_formula())
