from typing import List, Any, Union
import logging


class Node:
    def __init__(self, children: List = []):
        self._parent = None
        self._label_dict = {}
        self._children = [None] * len(children)
        for i, child in enumerate(children):
            self.set_child(i, child)

    def repr_node(self) -> Union[str, int]:
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
        logging.error("Child {} not accepted by {} at index {}"
                      .format(child, self, index))
        return None

    def set(self, child: "Node") -> "Node":
        return self.set_child(0, child)

    def set_left(self, child: "Node") -> "Node":
        return self.set_child(0, child)

    def set_right(self, child: "Node") -> "Node":
        return self.set_child(1, child)

    def set_binary(self, left: "Node", right: "Node") -> "Node":
        self.set_left(left)
        return self.set_right(right)

    def set_label(self, key: Any, value: Any) -> None:
        assert key not in self._label_dict, "Nodes cannot be relabelled"
        self._label_dict[key] = value

    def label(self, key: Any, value: Any) -> Any:
        return self._label_dict[key]
