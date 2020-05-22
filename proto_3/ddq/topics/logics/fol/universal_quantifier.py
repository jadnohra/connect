from ddq.topics.logics.logic import Formulator
from ddq.util.check_type import check_type
from .universal_variable import UniversalVariable
from .quantifier import Quantifier
from .statement import StatementDuck


class UniversalQuantifierForumulator(Formulator):
    def __call__(self, *parameters):
        return UniversalQuantifier(*parameters)


class UniversalQuantifier(Quantifier):
    def __init__(self, *children):
        super().__init__([UniversalVariable, StatementDuck])
        self.overwrite_children(children)

    def repr_node(self) -> str:
        return "∀"

    def accepts_child(self, index: int, child: "Node") -> bool:
        type_checks = {
            0: UniversalVariable, 
            1: StatementDuck.types()
        }
        return check_type(child, type_checks[index])
