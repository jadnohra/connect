from .node import Node


class Axiom:
    def get_name(self) -> str:
        pass

    def get_formula(self) -> Node:
        pass

    def __call__(self):
        return self.get_formula()
