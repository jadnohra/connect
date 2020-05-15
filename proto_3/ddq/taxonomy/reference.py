from typing import List, Tuple

Author = Tuple[str, str]

class Reference:
    def __init__(self, name: str = "", 
                 authors: List[Author] = [], 
                 referenced_parts: List = [str]):
        self._name = name
        self._authors = authors
        self._referenced_parts = referenced_parts
        
    def name(self) -> str:
        return self._name
    
    def authors(self) -> List[Author]:
        return self._authors
    
    def referenced_parts(self) -> List[str]:
        return self.referenced_parts
