from types import SimpleNamespace
from typing import List, Any
from ddq.inductor import Inductor
from ddq.definition import Definition, Defined, Node
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
        return InductiveFormation(inductive_index)(*children)


class InductiveFormationDefinition(Definition):
    def __init__(self, index: int, FOL: SimpleNamespace, ST: SimpleNamespace):
        def recurse_create_forall(count: int,
                                  vars: VarBuilder, 
                                  index: int = 0) -> Node:
            if index == count:
                return None
            else:
                return FOL.Forall(
                        vars.universal("u_{}".format(index)),
                        recurse_create_forall(count, vars, index+1))
        def recurse_create_or(count: int,
                              check_var: str,
                              vars: VarBuilder, 
                              index: int = 0) -> Node:
            eq_formula = FOL.Eq(vars[check_var], vars["u_{}".format(index)])
            if index + 1 == count:
                return eq_formula 
            else:
                return FOL.Or(
                        eq_formula,
                        recurse_create_or(count, check_var, vars, index+1))
        self._defined = (ST.InductiveFormation, 3)
        vars = VarBuilder()
        root_member_foralls = recurse_create_forall(index, vars)
        tail_member_foralls = root_member_foralls
        while tail_member_foralls.right() is not None:
            tail_member_foralls = tail_member_foralls.right()
        members = vars.values()
        tail_member_foralls.set_right(
            FOL.Forall(
                vars.universal("Set"),
                FOL.Equiv(
                    FOL.Eq(
                        vars["Set"],
                        ST.InductiveFormation(index, *members)
                    ),
                    FOL.Forall(
                        vars.universal("x"),
                        FOL.Equiv(
                            ST.In(vars["x"], vars["Set"]),
                            recurse_create_or(index, "x", vars)
                        )
                    )
                )
            )
        )
        self._formula = root_member_foralls
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
