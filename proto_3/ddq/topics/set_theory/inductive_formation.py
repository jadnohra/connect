from ddq.taxonomy.node import Node, NodeRepr
from ddq.topics.topic import Topic
from ddq.topics.logics.topic import Logic
from ddq.topics.logics.logic import Definition, Formulator, Term
from ddq.topics.logics.logic import Function as LogicalFunction 
from ddq.util.check_type import check_type


class InductiveFormationFormulator(Formulator):
    def __call__(self, *parameters) -> Node:
        return InductiveFormation(*parameters)
    
    
class InductiveFormation(LogicalFunction):
    def __init__(self, *in_children):
        super().__init__()
        self.set_children(in_children)
        
    def accepts_child(self, index: int, child: "Node") -> bool:
        return check_type(child, Term)
        
    @staticmethod
    def symbol() -> str:
        return "{}"
    
    def repr_node(self) -> NodeRepr:
        return self.symbol()


class InductionFormationDefinitionInductor(Definition):
    def __init__(self, FOL: Logic, ST: Topic):
        self._fol = FOL
        self._st = ST

    def create_definition_node(self, induction_length: int):
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
        # TBC continue here, we are just about re-adding the FOL quantifier to FOL
        self._defined = (ST.InductiveFormation, [Term]*induction_length)
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

    def __call__(self, *parameters) -> Node:
        return self.create_definition_node(*parameters)


