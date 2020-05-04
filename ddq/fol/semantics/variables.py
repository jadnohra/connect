from .types import DiscourseType, FunctionalType, Term, TermTuple
from .thing import Thing


class Variable(Thing):
    def functional_type(self) -> FunctionalType:
        return FunctionalType(Term, None)


class BoundVariable(Variable):
    pass


class SpecificVariable(Variable):
    pass


class UniqueVariable(Variable):
    pass


class AssumptionVariable(Variable):
    pass


class ArbitraryVariable(Variable):
    pass
