from types import SimpleNamespace
from typing import List
from ddq.definition import Definition, Defined, Node
from ddq.fol.predicate import Predicate
from ddq.fol.function import Function
from ddq.var_builder import VarBuilder


class Powerset(Function):
    def __init__(self):
        super().__init__('𝒫', 1)

    def notes(self) -> List[str]:
        return ["Not essential, definitionally replacable"]


class PowersetDefinition(Definition):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        self._defined = ST.Subset
        vars = VarBuilder()
        self._formula = (
            FOL.Forall(
                vars.universal("Powerset"),
                FOL.Forall(
                    vars.universal("Set"),
                    FOL.Equiv(
                        FOL.Eq(
                            vars["Powerset"],
                            ST.Powerset(
                                vars["Set"]
                            )
                        ),
                        FOL.Forall(
                            vars.universal("u"),
                            FOL.Equiv(
                                ST.Subset(vars["u"], vars["Set"]),
                                ST.In(vars["u"], vars["Powerset"]),
                            )
                        )
                    )
                )
            )
        )
        pass

    def get_defined(self) -> Defined:
        return self._defined

    @staticmethod
    def name() -> str:
        return "Power Definition"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
