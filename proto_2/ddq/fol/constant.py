from ddq.node import Instantiator
from .variable import VariableDeclarationNode, VarInhabitance


class Constant(Instantiator):
    def __init__(self, symbol: str):
        self._symbol = symbol

    def symbol(self) -> str:
        return self._symbol

    def __call__(self):
        return ConstantNode(self)


class ConstantNode(VariableDeclarationNode):
    def __init__(self, constant: Constant):
        super().__init__(VarInhabitance.UNIQUE)
        self._constant = constant

    def repr_node(self) -> str:
        return self._constant.symbol()
