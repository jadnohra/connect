'''
References:
 - Symbolic Logic, Copi, p.33, 396
'''
from typing import List
from .lang import (
    PropositionalVariable,
    Wff, PropVarWff, ImplWff, ConjWff, DisjWff, NegWff)
from .inference import Inference


class PropInference(Inference):
    def __init__(self, premisses: List[Wff], conclusion: List[Wff]):
        self.premisses = premisses
        self.conclusion = conclusion

    def short_name(self):
        pass


class ModusPonens(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = ImplWff(p, q)
        prem2 = p
        concl = q
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'MP'

    def possible_inferences(self, permisses: List[Wff]):
        pass


class ModusTollens(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = ImplWff(p, q)
        prem2 = NegWff(q)
        concl = NegWff(p)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'MT'


class HypotheticalSyllogism(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        prem1 = ImplWff(p, q)
        prem2 = ImplWff(q, r)
        concl = ImplWff(p, r)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'HS'


class DisjunctiveSyllogism(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = DisjWff(p, q)
        prem2 = NegWff(q)
        concl = q
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DS'


class ConstructiveDilemma(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        s = PropVarWff(PropositionalVariable('s'))
        prem1 = DisjWff(
                    ImplWff(p, q),
                    ImplWff(r, s))
        prem2 = DisjWff(p, r)
        concl = DisjWff(q, s)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DS'


class DistructuveDilemma(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        s = PropVarWff(PropositionalVariable('s'))
        prem1 = DisjWff(
                    ImplWff(p, q),
                    ImplWff(r, s))
        prem2 = DisjWff(
                    NegWff(q),
                    NegWff(s))
        concl = DisjWff(
                    NegWff(p),
                    NegWff(r))
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DD'


class Simplification(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem = ConjWff(p, q)
        concl = q
        super().__init__([prem], [concl])

    def short_name(self):
        return 'SIMP'


class Conjunction(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = p
        prem2 = q
        concl = ConjWff(p, q)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'CONJ'


class Addition(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem = p
        concl = DisjWff(p, q)
        super().__init__([prem], [concl])

    def short_name(self):
        return 'ADD'
