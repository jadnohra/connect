'''
References:
 - Symbolic Logic, Copi, p.33, 396
'''
from typing import List
from .fol_lang import Wff, PropVarWff, BinaryWff, PropositionalVariable, NegWff


class Inference:
    def short_name(self):
        pass

    def possible_inferences(self, permisses: List[Wff]):
        pass


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
        prem1 = BinaryWff.new_impl(p, q)
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
        prem1 = BinaryWff.new_impl(p, q)
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
        prem1 = BinaryWff.new_impl(p, q)
        prem2 = BinaryWff.new_impl(q, r)
        concl = BinaryWff.new_impl(p, r)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'HS'


class DisjunctiveSyllogism(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem1 = BinaryWff.new_disj(p, q)
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
        prem1 = BinaryWff.new_disj(
                    BinaryWff.new_impl(p, q),
                    BinaryWff.new_impl(r, s))
        prem2 = BinaryWff.new_disj(p, r)
        concl = BinaryWff.new_disj(q, s)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'DS'


class DistructuveDilemma(PropInference):
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


class Simplification(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem = BinaryWff.new_conj(p, q)
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
        concl = BinaryWff.new_conj(p, q)
        super().__init__([prem1, prem2], [concl])

    def short_name(self):
        return 'CONJ'


class Addition(PropInference):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        prem = p
        concl = BinaryWff.new_disj(p, q)
        super().__init__([prem], [concl])

    def short_name(self):
        return 'ADD'


class Replacement:
    def __init__(self, pattern1: Wff, pattern2: Wff):
        self.pattern1 = pattern1
        self.pattern2 = pattern2

    def short_name(self):
        pass


class DeMorganConj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = NegWff(BinaryWff.new_conj(p, q))
        pat2 = BinaryWff.new_disj(
                NegWff(p),
                NegWff(q))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'DMc'


class DeMorganDisj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = NegWff(BinaryWff.new_disj(p, q))
        pat2 = BinaryWff.new_conj(
                NegWff(p), 
                NegWff(q))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'DMd'


class CommutationConj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = BinaryWff.new_conj(p, q)
        pat2 = BinaryWff.new_conj(q, p)
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'COMc'


class CommutationDisj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = BinaryWff.new_disj(p, q)
        pat2 = BinaryWff.new_disj(q, p)
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'COMd'


class AssociationConj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        pat1 = BinaryWff.new_conj(
                BinaryWff.new_conj(p, q),
                r)
        pat2 = BinaryWff.new_conj(
                p,
                BinaryWff.new_conj(q, r))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'ASCc'


class AssociationDisj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        pat1 = BinaryWff.new_disj(
                BinaryWff.new_disj(p, q),
                r)
        pat2 = BinaryWff.new_disj(
                p,
                BinaryWff.new_disj(q, r))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'ASCd'


class DistributionConj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        pat1 = BinaryWff.new_conj(
                p,
                BinaryWff.new_disj(q, r))
        pat2 = BinaryWff.new_disj(
                BinaryWff.new_conj(p, q),
                BinaryWff.new_conj(p, r))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'DISTc'


class DistributionDisj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        pat1 = BinaryWff.new_disj(
                p,
                BinaryWff.new_conj(q, r))
        pat2 = BinaryWff.new_conj(
                BinaryWff.new_disj(p, q),
                BinaryWff.new_disj(p, r))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'DISTd'


class DoubleNegation(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        pat1 = NegWff(NegWff(p))
        pat2 = p
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'DN'


class Transposition(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = BinaryWff.new_impl(p, q)
        pat2 = BinaryWff.new_impl(NegWff(q), NegWff(p))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'TRANS'


class MaterialImplication(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = BinaryWff.new_impl(p, q)
        pat2 = BinaryWff.new_disj(NegWff(p), q)
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'IMPL'


class MaterialEquivalenceConj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = BinaryWff.new_equiv(p, q)
        pat2 = BinaryWff.new_conj(
                BinaryWff.new_impl(p, q),
                BinaryWff.new_impl(q, p)
                )
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'EQUIVc'


class MaterialEquivalenceDisj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        pat1 = BinaryWff.new_equiv(p, q)
        pat2 = BinaryWff.new_disj(
                BinaryWff.new_conj(p, q),
                BinaryWff.new_conj(NegWff(q), NegWff(q))
                )
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'EQUIVd'


class Exportation(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        q = PropVarWff(PropositionalVariable('q'))
        r = PropVarWff(PropositionalVariable('r'))
        pat1 = BinaryWff.new_impl(
                BinaryWff.new_conj(p, q),
                r)
        pat2 = BinaryWff.new_impl(
                p,
                BinaryWff.new_impl(q, r))
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'EXP'


class TautologyConj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        pat1 = p
        pat2 = BinaryWff.new_conj(p, p)
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'TAUTc'


class TautologyDisj(Replacement):
    def __init__(self):
        p = PropVarWff(PropositionalVariable('p'))
        pat1 = p
        pat2 = BinaryWff.new_conj(p, p)
        super().__init__(pat1, pat2)

    def short_name(self):
        return 'TAUTd'
