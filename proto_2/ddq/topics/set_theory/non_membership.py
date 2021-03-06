from types import SimpleNamespace
from typing import List
from ddq.node import Node
from ddq.definition import Definition
from ddq.var_builder import VarBuilder
from ddq.fol.predicate import Predicate


class NonMembership(Predicate):
    def __init__(self):
        super().__init__('∉', 2)

    def notes(self) -> List[str]:
        return ["Not essential, definitionally replacable by membership"]


class NonMembeshipDefinition(Definition):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        self._defined = ST.Nin
        vars = VarBuilder()
        self._formula = (
            FOL.Forall(
                vars.universal('u'),
                FOL.Forall(
                    vars.universal('v'),
                    FOL.Equiv(
                        ST.In(
                            vars['u'], vars['v']
                        ),
                        FOL.Not(
                            ST.Nin(
                                vars['u'], vars['v']
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
        return "Non-membership definition"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
