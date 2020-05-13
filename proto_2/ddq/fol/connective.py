from ddq.node import Node, Instantiator
from .node_types import is_term, is_variable_declaration


class Connective(Instantiator):
    def __init__(self, symbol: str, arity: int, node_class: type):
        self._symbol = symbol
        self._arity = arity
        self._node_class = node_class

    def arity(self) -> int:
        return self._arity

    def symbol(self) -> str:
        return self._symbol

    def __call__(self, *children):
        return self._node_class(self, *children)


class ConnectiveNode(Node):
    def __init__(self, connective: Connective, *children):
        full_children = (list(children)
                         + ([None] * (connective.arity() - len(children))))
        super().__init__(*full_children)
        self._connective = connective

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        return not any(is_type(child)
                       for is_type in [is_term, is_variable_declaration])

    def repr_node(self) -> str:
        return self._connective.symbol() if self._connective else None
