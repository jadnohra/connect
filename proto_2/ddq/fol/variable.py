from enum import Enum, auto
from ddq.node import Node, NodeRepr


class VarInhabitance(Enum):
    UNIVERSAL = auto()
    EXISTENTIAL = auto()
    ASSUMED = auto()
    UNIQUE = auto()


class VariableDeclarationNode(Node):
    def __init__(self, 
                 inhabitance: VarInhabitance = None, 
                 default_symbol = None):
        super().__init__()
        self._inhabitance = inhabitance
        self._default_symbol = default_symbol

    def repr_node(self) -> NodeRepr:
        return (self._default_symbol if self._default_symbol is not None
                else super().repr_node())

    def validate(self,
                 ensureFullyBuilt: bool = False,
                 validateChildren: bool = False):
        if self.parent() is not None:
            assert(self._inhabitance is not None)
        super().validate(ensureFullyBuilt, validateChildren)

    def inhabitance(self) -> VarInhabitance:
        self._inhabitance

    def __call__(self):
        return VariableNode(self)


class VariableNode(Node):
    def __init__(self, declaration: VariableDeclarationNode = None):
        super().__init__()
        self._declaration = declaration

    def inhabitance(self) -> VarInhabitance:
        self._declaration.inhabitance()

    def repr_node(self) -> str:
        return self._declaration if self._declaration else super().repr_node()


def var_universal(default_symbol = None) -> VariableDeclarationNode:
    return VariableDeclarationNode(VarInhabitance.UNIVERSAL, 
                                   default_symbol = default_symbol)


def var_existential(default_symbol = None) -> VariableDeclarationNode:
    return VariableDeclarationNode(VarInhabitance.EXISTENTIAL,
                                   default_symbol = default_symbol)


def var(decl_node: VariableDeclarationNode) -> VariableNode:
    return VariableNode(decl_node)
