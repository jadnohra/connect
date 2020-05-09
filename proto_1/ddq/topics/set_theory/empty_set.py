from ddq.fol.constant import Constant
from ddq.axiom import Axiom, Node
from ddq.fol.variable import universal_var, var, VarBuilContext
from ddq.fol.quantifier import forall
from ddq.fol.natural_deduction.import_all import *
from .empty_set import st_in


class EmptySetConstant(Constant):
    def __init__(self):
        super().__init__("∅")


class EmptySetAxiom(Axiom):
    def __init__(self, empty_set_constant: EmptySetConstant):
        vars = VarBuilContext()
        self._formula = (
            forall()
            .set_left(vars.declare('x', universal_var()))
            .set_right(
                l_not()
                .set(
                    st_in()
                    .set_left(vars.reference('x'))
                    .set_right(var(empty_set_constant))
                )
            )
        )
        pass

    def get_name(self) -> str:
        return "Empty Set"

    def get_formula(self) -> Node:
        pass
