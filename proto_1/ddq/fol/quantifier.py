from ddq.node import Node
from .node_types import is_variable_declaration, is_predicate, is_connective


class QuantifierNode(Node):
    def __init__(self):
        super().__init__([None, None])

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        if index == 0:
            return is_variable_declaration(child)
        if index == 1:
            return is_predicate(child) or is_connective(child)


class UniversalQuantifierNode(QuantifierNode):
    def repr_node(self) -> str:
        return "∀"


class ExistentialQuantifierNode(QuantifierNode):
    def repr_node(self) -> str:
        return "∃"


def forall() -> UniversalQuantifierNode:
    return UniversalQuantifierNode()


def exists() -> ExistentialQuantifierNode:
    return ExistentialQuantifierNode()
