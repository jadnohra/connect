import types
from typing import Any
from .equality import Equality
from .quantifier import UniversalQuantifier, ExistentialQuantifier


def build_topic() -> Any:
    fol = types.SimpleNamespace()
    fol.eq = Equality()
    fol.forall = UniversalQuantifier()
    fol.exists = ExistentialQuantifier()
    return fol


FOL = build_topic()
