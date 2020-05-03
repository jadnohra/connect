from .node import NamedNonLeafNode, classproperty


class Wff:
    def __init__(self):
        pass


class Term:
    def __init__(self):
        pass

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
