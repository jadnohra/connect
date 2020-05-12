from types import SimpleNamespace
from typing import List
from ddq.definition import Definition, Node
from ddq.fol.predicate import Predicate
from ddq.var_builder import VarBuilder


class Subset(Predicate):
    def __init__(self):
        super().__init__('⊆', 2)

    def notes(self) -> List[str]:
        return ["Not essential, definitionally replacable"]


class SubsetDefinition(Definition):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        self._defined = ST.Subset
        vars = VarBuilder()
        self._formula = (
            FOL.Forall(
                vars.universal("Set"),
                FOL.Forall(
                    vars.universal("Subset"),
                    FOL.Equiv(
                        ST.Subset(vars["Subset"], vars["Set"]),
                        FOL.Forall(
                            vars.universal("u"),
                            FOL.Impl(
                                ST.In(vars["u"], vars["Subset"]),
                                ST.In(vars["u"], vars["Set"]),
                            )
                        )
                    )
                )
            )
        )
        pass
    
    def get_defined(self) -> Predicate:
        return self._defined

    @staticmethod
    def name() -> str:
        return "Subset Definition"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
