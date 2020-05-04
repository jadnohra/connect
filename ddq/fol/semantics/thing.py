from abc import ABC, abstractmethod
from .types import FunctionalType


class Thing(ABC):
    @abstractmethod
    def functional_type(self) -> FunctionalType:
        pass

    def get_functional_input(self) -> "Thing":
        pass
