from ddq.node import Node, Instantiator
from .node_types import (
    is_variable_declaration,
    is_predicate,
    is_connective,
    is_quantifier)


class UniversalQuantifierForumulator(Formulator):
    def __init__(self, symbol: str, node_class: type):
        self._symbol = symbol
        self._node_class = node_class

    def symbol(self) -> str:
        return UniversalQuantifier.symbol()

    def __call__(self, *parameters):
        return UniversalQuantifier(*parameters)


class UniversalQuantifier(Node):
    def __init__(self, *children):
        super().__init__(children)

    @staticmethod
    def symbol() -> str:
        return "{}"

    def repr_node(self) -> str:
        return self.symbol()

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        if index == 0:
            return is_variable_declaration(child)
        if index == 1:
            return any(is_type(child) for is_type in
                       [is_predicate, is_connective, is_quantifier])


    