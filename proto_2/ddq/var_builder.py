from typing import Any, List
from .builder import Builder
from ddq.fol.variable import (
    var_universal,
    var_existential,
    VariableNode,
    VariableDeclarationNode)


class VarBuilder(Builder):
    def universal(self, name: str) -> VariableDeclarationNode:
        return self.put(name, var_universal())

    def existential(self, name: str) -> VariableDeclarationNode:
        return self.put(name, var_existential())

    def __getitem__(self, name: str) -> VariableNode:
        return self.get(name)()

    def values(self) -> List[VariableNode]:
        return [self[x] for x in self.keys()]
