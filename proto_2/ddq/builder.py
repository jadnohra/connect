from typing import Any


class Builder:
    def __init__(self):
        self._dict = {}

    def put(self, name: str, object: Any) -> Any:
        assert name not in self._dict
        self._dict[name] = object
        return object

    def get(self, name: str) -> object:
        return self._dict[name]
