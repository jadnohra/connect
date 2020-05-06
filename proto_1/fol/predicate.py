from typing import List
from .node import Node


class Predicate:
    def __init__(self, symbol: str, arity: int):
        self._symbol = symbol
        self._arity = arity

    def new_node(self) -> type:
        return PredicateNode


class PredicateNode(Node):
    def __init__(self, predicate: Predicate):
        self._predicate = predicate
        self._children = [None] * predicate.arity()

    def children(self) -> List:
        return self._children

    def setChild(self, index: int, child: Node) -> bool:
        if not child.is_term():
            return False
        self._children[index] = child
        return True

    def setLeft(self, child: Node) -> bool:
        return self.setChild(0, child)

    def setRight(self, child: Node) -> bool:
        return self.setChild(1, child)
