from .types import FunctionalType, Term, TermTuple
from .thing import Thing


class Function(Thing):
    def __init__(self, arity: int):
        super().__init__()
        self._functional_type = FunctionalType(Term, TermTuple(arity))

    def arity(self) -> int:
        return self._functional_type.from_type().arity()

    def functional_type(self) -> FunctionalType:
        return self._functional_type
