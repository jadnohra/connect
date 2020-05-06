from enum import Enum, auto
from ..node import Node


class VarInhabitance(Enum):
    UNIVERSAL = auto()
    EXISTENTIAL = auto()
    ASSUMED = auto()


class VariableDeclarationNode(Node):
    def __init__(self, inhabitance: VarInhabitance = None):
        self._inhabitance = inhabitance

    def validate(self,
                 ensureFullyBuilt: bool = False,
                 validateChildren: bool = False):
        if self.parent() is not None:
            assert(self._inhabitance is not None)
        super().validate(ensureFullyBuilt, validateChildren)

    def inhabitance(self) -> VarInhabitance:
        self._inhabitance


class VariableNode(Node):
    def __init__(self, declaration: VariableDeclarationNode = None):
        self._declaration = declaration

    def is_term(self) -> bool:
        return True

    def inhabitance(self) -> VarInhabitance:
        self._declaration.inhabitance()
