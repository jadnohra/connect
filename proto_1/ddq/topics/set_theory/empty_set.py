from typing import List
from ddq.fol.constant import Constant
from ddq.axiom import Axiom, Node
from ddq.builder import Builder
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
        build = Builder()
        self._formula = (
            forall()
            .set_left(build.put('x', universal_var()))
            .set_right(
                l_not()
                .set(
                    st_in()
                    .set_left(var(build.get('x')))
                    .set_right(var(empty_set_constant))
                )
            )
        )
        pass

    @staticmethod
    def name() -> str:
        return "Empty Set"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
