from .node import Node


class Variable:
    def __init__(self):
        self._symbol = symbol
        self._arity = arity

    def new_node(self) -> type:
        return VariableNode


class VariableNode(Node):
    def __init__(self, predicate: Predicate):
        self._predicate = predicate
        self._children = [None] * predicate.arity()