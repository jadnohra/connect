from ddq.taxonomy.thing import Thing
from ddq.taxonomy.node import Node


class Function(Node):
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
