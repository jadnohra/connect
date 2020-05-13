from types import SimpleNamespace
from typing import List, Any
from ddq.node import Instantiator
from ddq.fol.node_types import is_function, is_predicate
from ddq.fol.predicate import Predicate
from ddq.definition import Definition, Defined, Node
from ddq.var_builder import VarBuilder


class FunctionDefinitionOperator(Instantiator):
    def notes(self) -> List[str]:
        return ["Syntactic sugar"]
    
    def symbol(self) -> str:
        return '≜'
    
    def arity(self) -> int:
        return 2
    
    def __call__(self, *children):
        pass


class FunctionDefinitionOperatorNode(Node):
    def __init__(self, def_op: FunctionDefinitionOperator, *children):
        # Build full children by taking the passed-in children
        #  and completing up to arity with None children.
        full_children = (list(children)
                         + ([None] * (def_op.arity() - len(children))))
        super().__init__(*full_children)
        self._def_op = def_op

    def accepts_child(self, index: int, child: "Node") -> bool:
        if child is None:
            return True
        if index == 0:
            return is_function(child)
        elif index == 1:
            return is_predicate(child)
        return False

    def repr_node(self) -> str:
        return self._def_op.symbol() if self._def_op else None

    def notes(self) -> List[str]:
        return []


class DefinitionOperationDefinition(Definition):
    def __init__(self, FOL: SimpleNamespace, ST: SimpleNamespace):
        self._defined = FOL.DefOp
        vars = VarBuilder()
        # TODO: the problem here that this node depends on the function being defined
        # So it can only be applied based on a concrete function definition? or can we provide 
        # a recipe?
        # making this work nicely needs a refactoring, every entity eg function must be expressible as a partially-expanded parametrizable 
        # node
        # TBC
        self._formula = (
            FOL.Forall(
                vars.universal("f"),
                FOL.Equiv(
                    FOL.Eq(
                        vars["f"],
                        None
                    ),
                    None
                )
            )
        )
        pass
    
    def get_defined(self) -> Predicate:
        return self._defined

    @staticmethod
    def name() -> str:
        return "Definition Operator definition"

    def get_name(self) -> str:
        return self.name()

    def get_formula(self) -> Node:
        return self._formula
