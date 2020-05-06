from ..node import Node
from .node_types import is_term


class Predicate:
    def __init__(self, symbol: str, arity: int):
        self._symbol = symbol
        self._arity = arity

    def symbol(self) -> str:
        return self._symbol

    def new_node(self) -> Node:
        return PredicateNode(self)


class PredicateNode(Node):
    def __init__(self, predicate: Predicate):
        super().__init__([None] * predicate.arity())
        self._predicate = predicate

    def acceptChild(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        return is_term(child)

    def repr_node(self) -> str:
        return self._predicate.symbol() if self._predicate else None
def repr_node(self) -> str:
