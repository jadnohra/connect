from typing import List


class Node:
    def __init__(self, children: List = []):
        self._parent = None
        self._children = [None] * len(children)
        for i, child in enumerate(children):
            self.setChild(i, child)

    def repr_node(self) -> str:
        return id(self)

    def validate(self,
                 ensureFullyBuilt: bool = False,
                 validateChildren: bool = False):
        if validateChildren and self.children() is not None:
            if ensureFullyBuilt:
                assert all([x is not None for x in self.children()])
            for child in self.children():
                child.validate(ensureFullyBuilt, validateChildren)

    def onChildChanged(self):
        pass

    def onChanged(self):
        if self._parent is not None:
            self._parent.onChildChanged(self)

    def parent(self) -> "Node":
        return None

    def children(self) -> List:
        return self._children

    def arity(self) -> int:
        return len(self.children()) if self.children() is not None else 0

    def acceptChild(self, index: int, child: "Node") -> bool:
        return True

    def setChild(self, index: int, child: "Node") -> "Node":
        if self.acceptChild(index, child):
            self._children[index] = child
            self.onChanged()
            return self
        return None
