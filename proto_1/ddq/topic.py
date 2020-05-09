from typing import List
from ddq.fol.predicate import Predicate
from ddq.fol.constant import Constant
from ddq.axiom import Axiom


class Topic:
    def get_name(self):
        pass

    def get_predicates(self) -> List[Predicate]:
        return []

    def get_constants(self) -> List[Constant]:
        return []

    def get_axioms(self) -> List[Axiom]:
        return []

    def find_axioms(self, axiom_class: type) -> List[Axiom]:
        return [x for x in self.get_axioms() if isinstance(x, axiom_class)]

    def find_axiom(self, axiom_class: type) -> Axiom:
        candidates = self.find_axioms(axiom_class)
        assert len(candidates) == 1
        return candidates[0]