from .thing import Thing
from .term import Term


class Individual(Thing, Term):
    def __init__(self, arity: int):
        super().__init__()


class SpecificIndividual(Individual):
    pass


class UniqueIndividual(SpecificIndividual):
    pass


class AssumptionIndividual(Individual):
    pass


class ArbitraryIndividual(Individual):
    pass
