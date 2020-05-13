from typing import List
from ddq.node import Node, Instantiator
from .node_types import is_term


class Function(Instantiator):
    def __init__(self, symbol: str, arity: int):
        self._symbol = symbol
        self._arity = arity

    def arity(self) -> int:
        return self._arity

    def symbol(self) -> str:
        return self._symbol

    def __call__(self, *children):
        return FunctionNode(self, *children)


class FunctionNode(Node):
    def __init__(self, function: Function, *children):
        # Build full children by taking the passed-in children
        #  and completing up to arity with None children.
        full_children = (list(children)
                         + ([None] * (function.arity() - len(children))))
        super().__init__(*full_children)
        self._function = function

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        return is_term(child)

    def repr_node(self) -> str:
        return self._function.symbol() if self._function else None

    def notes(self) -> List[str]:
        return []
