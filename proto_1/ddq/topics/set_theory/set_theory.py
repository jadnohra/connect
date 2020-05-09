from ddq.universe import Universe
from ddq.topic import Topic, Predicate, Constant, List
from .membership import Membership
from .empty_set import EmptySet


class SetTheoryTopic:
    def __init__(self):
        self._predicates = [Membership()]
        self._constants = [EmptySet()]

    def get_predicates(self) -> List[Predicate]:
        return self._predicates

    def get_constants(self) -> List[Constant]:
        return self._constants
