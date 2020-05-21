from ddq.taxonomy.thing import Thing
from ddq.taxonomy.node import Node

class OperatorLike:
    pass


class FunctionLike(Node):
    pass


class ClassFunction(FunctionLike):
    pass

class Function(FunctionLike):
    pass


class Predicate(Node):
    pass


class Meta(Node):
    pass


class Formulator(Thing):
    def symbol(self) -> str:
        pass
    
    def __call__(self, *parameters) -> Node:
        pass
