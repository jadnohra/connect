from ..node import Node
from .node_types import is_variable_declaration, is_predicate


class QuantifierNode(Node):
    def __init__(self):
        super().__init__([None, None])

    def acceptChild(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        if index == 0:
            return is_variable_declaration(child)
        if index == 1:
            return is_predicate(child)


class UniversalQuantifierNode(QuantifierNode):
    def node_repr(self) -> str:
        return "∀"


class ExistentialQuantifierNode(QuantifierNode):
    def node_repr(self) -> str:
        return "∃"
