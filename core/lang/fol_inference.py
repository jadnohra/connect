'''
References:
 - Symbolic Logic, Copi, p.33, 396
'''
from typing import List
from  .fol_lang import Wff, PropVarWff, BinaryWff, PropositionalVariable


class Inference:
    def __init__(self, premisses: List[Wff], conclusion: List[Wff]):
        self.premisses = premisses
        self.conclusion = conclusion


class ModusPonens(Inference):
    def __init__(self):
        P = PropVarWff(PropositionalVariable('P'))
        Q = PropositionalVariable('Q')
        prem1 = BinaryWff.new_impl(P, Q)
        super().__init__()