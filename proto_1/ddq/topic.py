from typing import List
from ddq.fol.predicate import Predicate
from ddq.fol.constant import Constant
from ddq.axiom import Axiom
from ddq.definition import Definition


class Topic:
    def get_name(self):
        pass

    def get_references(self) -> List[str]:
        return []

    def get_predicates(self) -> List[Predicate]:
        return []

    def get_constants(self) -> List[Constant]:
        return []

    def get_axioms(self) -> List[Axiom]:
        return []

    def get_definitions(self) -> List[Definition]:
        return []

