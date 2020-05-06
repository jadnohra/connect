from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    def __init__(self):
        self._parent = None
    
    @abstractmethod
    def parent(self) -> "Node":
        return None

    @abstractmethod
    def children(self) -> List:
        return None

    def arity(self) -> int:
        return len(self.children()) if self.children() is not None else 0

    @abstractmethod
    def setChild(self, index: int, child: "Node") -> bool:
        return False
