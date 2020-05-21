import pytest
from .function_definition import PredicativeFunctionDefinitionFormulator
from ddq.util.print_tree import print_node


def test_function_definition():
    formulator = PredicativeFunctionDefinitionFormulator()
    print_node(formulator())