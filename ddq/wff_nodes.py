from abc import ABC, abstractmethod

from .node import (
    NamedNonLeafNode, NamedLeafNode, classproperty
)

# class hierarchies don't seem to be the best thing. Maybe we need just labels ...
# a 'component-entity' design or duck-typing.


class Wff(ABC):
    pass


class Term(Wff):
    pass


class Constant(NamedLeafNode, Term):
    @classproperty
    def typename(cls) -> str:
        return "constant"


class Predicate(NamedNonLeafNode, Wff):
    @classproperty
    def typename(cls) -> str:
        return "predicate"

    @classproperty
    def childtype(cls) -> type:
        return Term

    def __init__(self, arity: int):
        self._arity = arity
        self._children = [None]*arity
