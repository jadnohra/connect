from ddq.universe import Universe
from ddq.builder import Builder
from ddq.topic import Topic, Predicate, Constant, Axiom, List
from ddq.topic import Topic as BaseTopic
from .membership import Membership
from .empty_set import EmptySetConstant, EmptySetAxiom


class SetTheoryTopic(BaseTopic):
    def __init__(self):
        build = Builder()
        self._predicates = [Membership()]
        self._constants = [build.put("empty", EmptySetConstant())]
        self._axioms = [EmptySetAxiom(build.get("empty"))]

    def get_predicates(self) -> List[Predicate]:
        return self._predicates

    def get_constants(self) -> List[Constant]:
        return self._constants

    def get_axioms(self) -> List[Axiom]:
        return self._axioms


def topic() -> SetTheoryTopic:
    return SetTheoryTopic()
