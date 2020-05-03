from typing import Union, List
from .classproperty import classproperty


class Node:
    @property
    def children(self) -> List["Node"]:
        """Returns a list of children.
           Only valid when is_leaf is False."""
        pass

    @classproperty
    def is_leaf(cls) -> bool:
        """True if this node is a leaf"""
        pass

    @property
    def name(self) -> str:
        """A friendly name for this node.
           This is used for printing per example"""
        pass

    @classproperty
    def typename(cls) -> str:
        """A friendly name for the type of this node.
           This is used for printing per example"""
        pass


class LeafNode(Node):
    @classproperty
    def is_leaf(cls) -> bool:
        return True


class NonLeafNode(Node):
    def __init__(self):
        self._children = []
    
    @classproperty
    def is_leaf(cls) -> bool:
        return False

    @property
    def children(self) -> List["Node"]:
        return self._children


class NamedLeafNode(LeafNode):
    def __init__(self, name: str = None):
        self._name = None

    @property
    def name(self) -> str:
        return self._name


class NamedNonLeafNode(LeafNode):
    def __init__(self, name: str = None):
        super().__init__()
        self._name = None

    @property
    def name(self) -> str:
        return self._name