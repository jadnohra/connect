import pytest
from .inductive_formation import InductiveFormationFormulator
from ddq.util.print_tree import print_node


def test_function_definition():
    formulator = InductiveFormationFormulator()
    print_node(formulator())