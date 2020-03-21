'''
References:
 - Andrews, p.101
 - An Outline of Set Theory, Henle, p.17
'''

from . import fol_lang
from .theorem import Axiom


class EqualSymbol(fol_lang.ImproperSymbol):
    def __init__(self):
        fol_lang.PrimitiveSymbol.__init__('=')

    def symbol_type(self) -> str:
        return 'equals'

    @staticmethod
    def new() -> "EqualSymbol":
        return EqualSymbol()


class EqualReflexAxiom(Axiom):
    def __init__(self):
        x = fol_lang.IndividualVariable('x')
        base_wff = fol_lang.BinaryWff(x, EqualSymbol.new(), x)
        wff = fol_lang.QuantifierWff.new_universal(x, base_wff)
        super().__init__(wff)
