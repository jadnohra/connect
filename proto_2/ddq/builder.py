from typing import Any
from ddq.fol.variable import var, VariableNode


class Builder:
    def __init__(self):
        self._dict = {}

    def put(self, name: str, object: Any) -> Any:
        assert name not in self._dict
        self._dict[name] = object
        return object

    def get(self, name: str) -> object:
        return self._dict[name]

    def __getitem__(self, name: str) -> object:
        return self.get(name)


class VarBuilder(Builder):
    def __getitem__(self, name: str) -> VariableNode:
        return var(self._dict[name])
