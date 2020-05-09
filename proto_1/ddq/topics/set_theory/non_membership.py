from typing import List
from ddq.node import Node
from ddq.definition import Definition
from ddq.builder import Builder
from ddq.fol.predicate import Predicate
from ddq.fol.variable import universal_var, var
from ddq.fol.quantifier import forall
from ddq.fol.natural_deduction.import_all import *
from .membership import st_in


class NonMembership(Predicate):
    def __init__(self):
        super().__init__('∉', 2)

    def notes(self) -> List[str]:
        return ["Not essential, definitionally replacable by membership"]


def st_nin() -> Node:
    return NonMembership().new_node()


class NonMembeshipDefinition(Definition):
    def __init__(self):
        build = Builder()
        self._formula = (
            forall()
            .set_left(build.put('x', universal_var()))
            .set_right(
                forall()
                .set_left(build.put('y', universal_var()))
                .set_right(
                    l_equiv()
                    .set_left(
                        st_in()
                        .set_left(var(build.get('x')))
                        .set_right(var(build.get('y')))
                    )
                    .set_right(
                        l_not()
                        .set(
                            st_nin()
                            .set_left(var(build.get('x')))
                            .set_right(var(build.get('y')))
                        )
                    )
                )
            )
        )
        pass

    @staticmethod
    def name() -> str:
        return "Non-membership definition"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
