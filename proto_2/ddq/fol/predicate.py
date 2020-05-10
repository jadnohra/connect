from typing import List
from ddq.node import Node, Instantiator
from .node_types import is_term


class Predicate(Instantiator):
    def __init__(self, symbol: str, arity: int):
        self._symbol = symbol
        self._arity = arity

    def arity(self) -> int:
        return self._arity

    def symbol(self) -> str:
        return self._symbol

    def new_node(self) -> Node:
        return PredicateNode(self)

    def __call__(self, *children):
        return PredicateNode(self, *children)


class PredicateNode(Node):
    def __init__(self, predicate: Predicate, *children):
        # Build full children by taking the passed-in children
        #  and completing up to arity with None children.
        full_children = (list(children)
                         + ([None] * (len(children) - predicate.arity())))
        super().__init__(*full_children)
        self._predicate = predicate

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        return is_term(child)

    def repr_node(self) -> str:
        return self._predicate.symbol() if self._predicate else None

    def notes(self) -> List[str]:
        return []
