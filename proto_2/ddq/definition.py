from .node import Node
from ddq.fol.predicate import Predicate


class Definition:
    def get_name(self) -> str:
        pass

    def get_formula(self) -> Node:
        pass
    
    def get_defined(self) -> Predicate:
        pass
