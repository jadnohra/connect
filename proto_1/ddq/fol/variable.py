from enum import Enum, auto
from ddq.node import Node


class VarInhabitance(Enum):
    UNIVERSAL = auto()
    EXISTENTIAL = auto()
    ASSUMED = auto()
    UNIQUE = auto()


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


def universal_var() -> VariableDeclarationNode:
    return VariableDeclarationNode(VarInhabitance.UNIVERSAL)


def existential_var() -> VariableDeclarationNode:
    return VariableDeclarationNode(VarInhabitance.EXISTENTIAL)


def var(decl_node: VariableDeclarationNode) -> VariableNode:
    return VariableNode(decl_node)


class VarBuilContext:
    def __init__(self):
        self._dict = {}

    def declare(self, name: str, decl_node: VariableDeclarationNode) -> VariableDeclarationNode:
        assert name not in self._dict
        self._dict[name] = decl_node

    def reference(self, name: str) -> VariableNode:
        return var(self._dict[name])
