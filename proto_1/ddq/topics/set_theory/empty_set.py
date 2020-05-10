from typing import List
from ddq.fol.constant import Constant
from ddq.axiom import Axiom, Node
from ddq.builder import VarBuilder
from ddq.fol.variable import universal_var, var
from ddq.fol.quantifier import forall
from ddq.fol.natural_deduction.import_all import *
from .membership import st_in


class EmptySetConstant(Constant):
    def __init__(self):
        super().__init__("∅")

    def notes(self) -> List[str]:
        return ["Not essential, but very common and convenient"]


class EmptySetAxiom(Axiom):
    def __init__(self, empty_set_constant: EmptySetConstant):
        vars = VarBuilder()
        self._formula = (
            forall().set_binary(
                vars.put('x', universal_var()),
                l_not().set(
                    st_in().set_binary(
                        vars['x'],
                        var(empty_set_constant)
                    )
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
