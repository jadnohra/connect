from typing import List
from . import fol


class Theorem:
    def __init__(self, premisses: List[fol.Wff],
                 conclusions: List[fol.Wff]):
        self.premisses = premisses
        self.conclusions = conclusions


class Axiom(Theorem):
    def __init__(wff: fol.Wff):
        super().__init__([], [wff])
