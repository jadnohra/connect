import pytest
from .function_definition import PredicativeClassFunctionDefinitionFormulator
from ddq.util.print_tree import print_node


def test_function_definition():
    formulator = PredicativeClassFunctionDefinitionFormulator()
    print_node(formulator())