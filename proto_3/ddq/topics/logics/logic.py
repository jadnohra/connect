from ddq.taxonomy.reference import Reference
from ddq.taxonomy.thing import Thing, List
from ddq.taxonomy.node import Node
from ddq.topics.topic import Topic


class Logic(Topic):
    def references(self) -> List[Reference]:
        return [
            Reference("Classical and Nonclassical Logics", 
                      [("Eric", "Schechter")])
        ]


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
