from enum import Enum, auto
from ddq.node import Node


class VarInhabitance(Enum):
    UNIVERSAL = auto()
    EXISTENTIAL = auto()
    ASSUMED = auto()
    UNIQUE = auto()


class VariableDeclarationNode(Node):
    def __init__(self, inhabitance: VarInhabitance = None):
        super().__init__()
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
        super().__init__()
        self._declaration = declaration

    def inhabitance(self) -> VarInhabitance:
        self._declaration.inhabitance()

    def repr_node(self) -> str:
        return self._declaration.repr_node() if self._declaration else None


def universal_var() -> VariableDeclarationNode:
    return VariableDeclarationNode(VarInhabitance.UNIVERSAL)


def existential_var() -> VariableDeclarationNode:
    return VariableDeclarationNode(VarInhabitance.EXISTENTIAL)


def var(decl_node: VariableDeclarationNode) -> VariableNode:
    return VariableNode(decl_node)
