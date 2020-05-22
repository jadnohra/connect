from ddq.topics.logics.logic import Formulator, Predicate
from ddq.topics.logics.fol.connective import Connective
from ddq.topics.logics.fol.statement import StatementDuck
from ddq.util.check_type import check_type


class ConjunctionForumulator(Formulator):
    def __call__(self, *parameters):
        return Conjunction(*parameters)


class Conjunction(Connective):
    def __init__(self, *children):
        super().__init__([StatementDuck, StatementDuck])
        self.overwrite_children(children)

    def repr_node(self) -> str:
        return "∧"

    def accepts_child(self, index: int, child: "Node") -> bool:
        type_checks = {
            0: StatementDuck.types(), 
            1: StatementDuck.types()
        }
        return check_type(child, type_checks[index])
