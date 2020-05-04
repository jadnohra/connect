from abc import ABC, abstractmethod


class Thing:
    def __init__(self, id: str = None):
        self._id = id

    def id(self) -> str:
        return self._id

    def set_id(self, id: str):
        assert self._id is None, "Universe thing id should not be reset"
        self._id = id
