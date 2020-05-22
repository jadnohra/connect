from typing import Tuple
from ddq.topics.logics.logic import Predicate, Duck
from .quantifier import Quantifier
from .connective import Connective


class StatementDuck(Duck):
    @staticmethod
    def types() -> Tuple:
        return StatementTypes


StatementTypes = (Quantifier, Predicate, Connective, StatementDuck)
