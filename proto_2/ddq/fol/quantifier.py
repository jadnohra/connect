from ddq.node import Node, Instantiator
from .node_types import (
    is_variable_declaration,
    is_predicate,
    is_connective,
    is_quantifier)


class Quantifier(Instantiator):
    def __init__(self, symbol: str, node_class: type):
        self._symbol = symbol
        self._node_class = node_class

    def symbol(self) -> str:
        return self._symbol

    def __call__(self, *children):
        return self._node_class(self, *children)


class QuantifierNode(Node):
    def __init__(self, quantifier: Quantifier, *children):
        super().__init__(*children)
        self._quantifier = quantifier

    def repr_node(self) -> str:
        return self._quantifier.symbol()

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        if index == 0:
            return is_variable_declaration(child)
        if index == 1:
            return any(is_type(child) for is_type in
                       [is_predicate, is_connective, is_quantifier])


class UniversalQuantifierNode(QuantifierNode):
    pass


class ExistentialQuantifierNode(QuantifierNode):
    pass


class UniversalQuantifier(Quantifier):
    def __init__(self):
        super().__init__("∀", UniversalQuantifierNode)


class ExistentialQuantifier(Quantifier):
    def __init__(self):
        super().__init__("∃", ExistentialQuantifierNode)
