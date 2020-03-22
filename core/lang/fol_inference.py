'''
References:
 - Symbolic Logic, Copi, p.33, 396
'''
from typing import List
from .fol_lang import Wff, PropVarWff, BinaryWff, PropositionalVariable, NegWff


class Inference:
    def __init__(self, premisses: List[Wff], conclusion: List[Wff]):
        self.premisses = premisses
        self.conclusion = conclusion

    def short_name(self):
        pass


class ModusPonens(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = BinaryWff.new_impl(p, q)
        prem2 = p
        concl = q
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'MP'


class ModusTollens(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = BinaryWff.new_impl(p, q)
        prem2 = NegWff(q)
        concl = NegWff(p)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'MT'


class HypotheticalSyllogism(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        prem1 = BinaryWff.new_impl(p, q)
        prem2 = BinaryWff.new_impl(q, r)
        concl = BinaryWff.new_impl(p, r)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'HS'


class DisjunctiveSyllogism(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = BinaryWff.new_disj(p, q)
        prem2 = NegWff(q)
        concl = q
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DS'


class ConstructiveDilemma(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        s = PropVarWff(PropositionalVariable('s'))
        prem1 = BinaryWff.new_disj(
                    BinaryWff.new_impl(p, q),
                    BinaryWff.new_impl(r, s))
        prem2 = BinaryWff.new_disj(p, r)
        concl = BinaryWff.new_disj(q, s)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DS'


class DistructuveDilemma(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        s = PropVarWff(PropositionalVariable('s'))
        prem1 = BinaryWff.new_disj(
                    BinaryWff.new_impl(p, q),
                    BinaryWff.new_impl(r, s))
        prem2 = BinaryWff.new_disj(
                    NegWff(q), 
                    NegWff(s))
        concl = BinaryWff.new_disj(
                    NegWff(p), 
                    NegWff(r))
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DD'


class Simplification(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem = BinaryWff.new_conj(p, q)
        concl = q
        super().__init__([prem], [concl])

    def short_name(self):
        return 'SIMP'


class Conjunction(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = p
        prem2 = q
        concl = BinaryWff.new_conj(p, q)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'CONJ'


class Addition(Inference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem = p
        concl = BinaryWff.new_disj(p, q)
        super().__init__([prem], [concl])

    def short_name(self):
        return 'ADD'
