from .variable import VariableDeclarationNode, VarInhabitance


class Constant(VariableDeclarationNode):
    def __init__(self, symbol: str = None):
        super().__init__(VarInhabitance.UNIQUE)
        self._symbol = symbol

    def repr_node(self) -> str:
        return self._symbol if self._symbol is not None else super().repr_node()


def declare_constant(symbol: str) -> Constant:
    return Constant(symbol)
