from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    def children(self) -> List:
        pass
