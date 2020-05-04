from .thing import Thing


class Predicate(Thing):
    def __init__(self, arity: int):
        super().__init__()
        self._arity = arity
        self._terms = [None] * arity

    def arity(self) -> int:
        return self._arity
