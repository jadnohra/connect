from typing import List
from .reference import Reference


class Thing:
    def name(self) -> str:
        return type(self).__name__

    def info(self) -> str:
        return ""
    
    def notes(self) -> List[str]:
        return []
    
    def references(self) -> List[Reference]:
        return []
