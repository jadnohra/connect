from typing import Union, List
from .classproperty import classproperty


class Node:
    def __init__(self, name: str = None, children: List = None,
                 child_type: type = None):
        """Note: We adopt the convention that the children
        list being None signifies a leaf node.
        """
        self._name = None
        self._children = children

    @property
    def children(self) -> List["Node"]:
        """Returns a list of children.
           Only valid when is_leaf is False."""
        self._children

    @classproperty
    def is_leaf(cls) -> bool:
        """True if this node is a leaf"""
        self._children is None

    @property
    def name(self) -> str:
        """A friendly name for this node.
           This is used for printing per example"""
        return self._name

    @classproperty
    def typename(cls) -> str:
        """A friendly name for the type of this node.
           This is used for printing per example"""
        pass

    @classproperty
    def childtype(cls) -> type:
        """Type of this node's children.
        Only valid when is_leaf is False."""
        pass


class NonLeafNode(Node):
    def __init__(self, children: List):
        super().__init__(self, children=children)


class NamedLeafNode(Node):
    def __init__(self, name: str):
        super().__init__(self, name=name)


class NamedNonLeafNode(NonLeafNode):
    def __init__(self, name: str, children: List):
        super().__init__(name=name, children=children)
