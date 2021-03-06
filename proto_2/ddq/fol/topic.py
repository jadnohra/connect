from types import SimpleNamespace
from .equality import Equality
from .quantifier import UniversalQuantifier, ExistentialQuantifier
from .natural_deduction.negation import Negation
from .natural_deduction.conjunction import Conjunction
from .natural_deduction.disjunction import Disjunction
from .natural_deduction.implication import Implication
from .natural_deduction.equivalence import Equivalence
from .sugar.function_definition_operator import FunctionDefinitionOperator


def build_topic() -> SimpleNamespace:
    fol = SimpleNamespace()
    fol.references = [
        ("Symbolic Logic", "Copi"),
        ("Mathematical Logic", ("Chiswell", "Hodges")),
        ("Type Theory and Formal Proof", ("Geuvers", "Nederpelt")),
        ("An Introduction to Mathematical Logic and Type Theory", "Andrews")
    ]
    fol.Eq = Equality()
    fol.Forall = UniversalQuantifier()
    fol.Exists = ExistentialQuantifier()
    fol.Not = Negation()
    fol.And = Conjunction()
    fol.Or = Disjunction()
    fol.Impl = Implication()
    fol.Equiv = Equivalence()
    fol.FuncDef = FunctionDefinitionOperator()
    return fol


FOL = build_topic()
