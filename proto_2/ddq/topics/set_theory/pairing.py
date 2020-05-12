from types import SimpleNamespace
from typing import List
from ddq.fol.constant import Constant, ConstantNode
from ddq.axiom import Axiom, Node
from ddq.var_builder import VarBuilder


class PairingAxiom(Axiom):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        vars = VarBuilder()
        self._formula = (
            FOL.Forall(
                vars.universal('u'),
                FOL.Forall(
                    vars.universal('v'),
                    FOL.Exists(
                        vars.existential('Pair'),
                        FOL.Forall(
                            vars.existential('x'),
                            FOL.Equiv(
                                ST.In(vars['x'], vars['Pair']),
                                FOL.Or(
                                    FOL.Eq(vars['x'], vars['u']),
                                    FOL.Eq(vars['x'], vars['v']),
                                )
                            )
                        )
                    )
                )
            )
        )
        pass

    @staticmethod
    def name() -> str:
        return "Pairing Axiom"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
