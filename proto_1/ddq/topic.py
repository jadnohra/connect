from typing import List
from .universe import Universe
from ddq.fol.predicate import Predicate
from ddq.fol.constant import Constant


class Topic:
    def get_name(self):
        pass

    def get_predicates(self) -> List[Predicate]:
        return []

    def get_constants(self) -> List[Constant]:
        return []
