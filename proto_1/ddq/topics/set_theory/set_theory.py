from ddq.universe import Universe
from ddq.topic import Topic, Predicate, Constant, Formula, List
from .membership import Membership
from .empty_set import EmptySetConstant, EmptySetAxiom


class SetTheoryTopic:
    def __init__(self):
        self._predicates = [Membership()]
        self._constants = [EmptySetConstant()]
        self._axioms = [EmptySetAxiom()]

    def get_predicates(self) -> List[Predicate]:
        return self._predicates

    def get_constants(self) -> List[Constant]:
        return self._constants

    def get_axioms(self) -> List[Formula]:
        return self._axioms
