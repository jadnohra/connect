from typing import Any
from ddq.taxonomy.thing import Thing
from ddq.taxonomy.node import Node

class Term:
    pass

class Constant(Node, Term):
    pass


class Variable(Node, Term):
    pass


class Function(Node, Term):
    pass


class Predicate(Node):
    pass


class Meta(Node):
    pass


class Formulator(Thing):
    def __call__(self, *parameters) -> Node:
        pass


class Definition(Formulator):
    
    def get_defined(self) -> Any:
        pass


class Axiom(Formulator):
    pass