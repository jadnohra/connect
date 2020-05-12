from typing import Union
from .node import Node
from ddq.fol.predicate import Predicate
from ddq.fol.function import Function


Defined = Union[Predicate, Function]


class Definition:
    def get_name(self) -> str:
        pass

    def get_formula(self) -> Node:
        pass

    def get_defined(self) -> Defined:
        pass

    def __call__(self):
        return self.get_formula()
