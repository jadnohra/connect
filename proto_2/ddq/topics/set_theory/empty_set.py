from types import SimpleNamespace
from typing import List
from ddq.fol.constant import Constant, ConstantNode
from ddq.axiom import Axiom, Node
from ddq.var_builder import VarBuilder


class EmptySetConstant(Constant):
    def __init__(self):
        super().__init__("∅")

    def notes(self) -> List[str]:
        return ["Not essential, but very common and convenient"]


class EmptySetConstantNode(ConstantNode):
    def __init__(self):
        super().__init__(EmptySetConstant())


class EmptySetAxiom(Axiom):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        vars = VarBuilder()
        self._formula = (
            FOL.Forall(
                vars.universal('x'),
                ST.Nin(
                    vars['x'],
                    ST.Empty()
                )
            )
        )

    @staticmethod
    def name() -> str:
        return "Empty Set"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
