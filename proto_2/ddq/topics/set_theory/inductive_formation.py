from types import SimpleNamespace
from typing import List, Any
from ddq.inductor import Inductor
from ddq.definition import Definition, Defined, Node
from ddq.fol.predicate import Predicate
from ddq.fol.function import Function
from ddq.var_builder import VarBuilder


class InductiveFormation(Function):
    def __init__(self, index: int):
        super().__init__('{}_' + str(index), index)

    def notes(self) -> List[str]:
        return ["Syntactic sugar"]


class InductiveFormationInductor(Inductor):
    def get_type(self) -> Any:
        return InductiveFormation

    def __call__(self, inductive_index: int, *children) -> Node:
        return InductiveFormation(inductive_index)()


class InductiveFormationDefinition(Definition):
    def __init__(self, index: int, FOL: SimpleNamespace, ST: SimpleNamespace):
        self._defined = None  # TODO
        vars = VarBuilder()
        self._formula = (
            ST.Empty  # TODO
        )
        pass

    def get_defined(self) -> Defined:
        return self._defined

    @staticmethod
    def name() -> str:
        return "Inductive Formation Defintion"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula


class InductiveFormationDefinitionInductor(Inductor):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        self._fol = FOL
        self._st = ST

    def get_type(self) -> Any:
        return InductiveFormationDefinition

    def __call__(self, inductive_index: int, *children) -> Node:
        return InductiveFormationDefinition(
                    inductive_index, self._fol, self._st)()
