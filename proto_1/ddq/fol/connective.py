from ddq.node import Node
from .node_types import is_term, is_variable_declaration


class Connective:
    def __init__(self, symbol: str, arity: int, node_class: type):
        self._symbol = symbol
        self._arity = arity
        self._node_class = node_class

    def arity(self) -> int:
        return self._arity

    def symbol(self) -> str:
        return self._symbol

    def new_node(self) -> Node:
        return self._node_class(self)


class ConnectiveNode(Node):
    def __init__(self, connective: Connective):
        super().__init__([None] * connective.arity())
        self._connective = connective

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        return not any(is_type(child) 
                       for is_type in [is_term, is_variable_declaration])

    def repr_node(self) -> str:
        return self._connective.symbol() if self._connective else None
