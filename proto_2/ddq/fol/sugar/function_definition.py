from types import SimpleNamespace
from typing import List, Any
from ddq.fol.predicate import Predicate
'''
from ddq.inductor import Inductor
from ddq.definition import Definition, Defined, Node
from ddq.fol.function import Function
from ddq.var_builder import VarBuilder
'''


class FunctionDefinition(Predicate):
    def __init__(self):
        super().__init__('≣', 2)

    def notes(self) -> List[str]:
        return ["Syntactic sugar"]
