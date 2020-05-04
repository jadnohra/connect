from .types import FunctionalType, Formula, TermTuple
from .thing import Thing
from .variables import BoundVariable
from .algorithms import recurse_find_thing
from ddq.node import Node


class Quantifier(Thing):
    def functional_type(self) -> FunctionalType:
        return FunctionalType(Formula, Formula)

    def build(self, formula: Thing, variable: BoundVariable):
        if variable is not None:
            assert recurse_find_thing(formula, variable) is not None
        self._variable = variable
        self._formula = formula


'''
class Quantifier(Node):
    def __init__(self, bind_context: BindContext = None):
        self._bind_context = (BindContext()
                              if bind_context is None
                              else bind_context)
        self._variable = self._bind_context.new_variable()

    def variable(self) -> BoundVariable:
        return self._variable

    def bind_context(self) -> BindContext:
        return self._bind_context

    def children(self) -> List:
        pass


class UniversalQuantifier(Quantifier):
    def __init__(self, bind_context: BindContext = None):
        super().__init__(bind_context)


class ExistentialQuantifier(Quantifier):
    def __init__(self, bind_context: BindContext = None):
        super().__init__(bind_context)

'''