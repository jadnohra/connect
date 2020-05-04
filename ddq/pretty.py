from abc import ABC, abstractmethod


class PrettyType(ABC):
    @staticmethod
    @abstractmethod
    def typename() -> str:
        pass


class PrettyInstance(ABC):
    @abstractmethod
    def instancename(self) -> str:
        pass
