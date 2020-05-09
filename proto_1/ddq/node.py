from typing import List


class Node:
    def __init__(self, children: List = []):
        self._parent = None
        self._children = [None] * len(children)
        for i, child in enumerate(children):
            self.set_child(i, child)

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

    def on_child_changed(self):
        pass

    def on_changed(self):
        if self._parent is not None:
            self._parent.on_child_changed(self)

    def parent(self) -> "Node":
        return None

    def children(self) -> List:
        return self._children

    def arity(self) -> int:
        return len(self.children()) if self.children() is not None else 0

    def accepts_child(self, index: int, child: "Node") -> bool:
        return True

    def set_child(self, index: int, child: "Node") -> "Node":
        if self.accepts_child(index, child):
            self._children[index] = child
            self.on_changed()
            return self
        return None

    def set(self, child: "Node") -> "Node":
        return self.set_child(0, child)

    def set_left(self, child: "Node") -> "Node":
        return self.set_child(0, child)

    def set_right(self, child: "Node") -> "Node":
        return self.set_child(1, child)
