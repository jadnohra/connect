from ddq.topics.logics.logic import Formulator
from ddq.util.check_type import check_type
from .existential_variable import ExistentialVariable
from .quantifier import Quantifier
from .statement import StatementDuck


class ExistentialQuantifierForumulator(Formulator):
    def __call__(self, *parameters):
        return ExistentialQuantifier(*parameters)


class ExistentialQuantifier(Quantifier):
    def __init__(self, *children):
        super().__init__([ExistentialVariable, StatementDuck])
        self.overwrite_children(children)

    def repr_node(self) -> str:
        return "∃"

    def accepts_child(self, index: int, child: "Node") -> bool:
        type_checks = {
            0: ExistentialVariable, 
            1: StatementDuck.types()
        }
        return check_type(child, type_checks[index])
