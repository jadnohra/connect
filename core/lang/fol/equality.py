'''
References:
 - Andrews, p.101
 - An Outline of Set Theory, Henle, p.17
'''

from . import lang
from .theorem import Axiom


class EqualSymbol(lang.ImproperSymbol):
    def __init__(self):
        lang.PrimitiveSymbol.__init__('=')

    def symbol_type(self) -> str:
        return 'equals'

    @staticmethod
    def new() -> "EqualSymbol":
        return EqualSymbol()


class EqualReflexAxiom(Axiom):
    def __init__(self):
        x = lang.IndividualVariable('x')
        base_wff = lang.BinaryWff(x, EqualSymbol(), x)
        wff = lang.UniversalWff(x, base_wff)
        super().__init__(wff)
