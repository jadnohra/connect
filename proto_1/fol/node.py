from ..node import Node as BaseNode


class Node(BaseNode):
    def is_term(self) -> bool:
        return False
