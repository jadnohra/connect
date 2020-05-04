from .thing import Thing
from .term import Term


class Function(Thing, Term):
    def __init__(self, arity: int):
        super().__init__()
        self._arity = arity
        self._terms = [None] * arity

    def arity(self) -> int:
        return self._arity
