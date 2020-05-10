import types
from typing import Any
from .equality import Equality
from .quantifier import UniversalQuantifier, ExistentialQuantifier
from .natural_deduction.negation import Negation
from .natural_deduction.equivalence import Equivalence


def build_topic() -> Any:
    fol = types.SimpleNamespace()
    fol.Eq = Equality()
    fol.Forall = UniversalQuantifier()
    fol.Exists = ExistentialQuantifier()
    fol.Not = Negation()
    fol.Equiv = Equivalence()
    return fol


FOL = build_topic()
