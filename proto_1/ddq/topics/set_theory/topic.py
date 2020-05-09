from typing import List
from ddq.universe import Universe
from ddq.builder import Builder
from ddq.topic import Topic, Predicate, Constant, Axiom, Definition
from ddq.topic import Topic as BaseTopic
from .membership import Membership
from .empty_set import EmptySetConstant, EmptySetAxiom
from .non_membership import NonMembeshipDefinition

class SetTheoryTopic(BaseTopic):
    def __init__(self):
        build = Builder()
        self._predicates = [Membership()]
        self._constants = [build.put("empty", EmptySetConstant())]
        self._axioms = [EmptySetAxiom(build.get("empty"))]
        self._definitions = [NonMembeshipDefinition()]

    def get_references(self) -> List[str]:
        return ["Elements of Set Theory (Henle)"]

    def get_predicates(self) -> List[Predicate]:
        return self._predicates

    def get_constants(self) -> List[Constant]:
        return self._constants

    def get_axioms(self) -> List[Axiom]:
        return self._axioms

    def get_definitions(self) -> List[Definition]:
        return self._definitions


def topic() -> SetTheoryTopic:
    return SetTheoryTopic()
