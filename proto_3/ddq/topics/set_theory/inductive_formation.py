from ddq.taxonomy.node import Node, NodeRepr
from ddq.topics.logics.logic import Formulator, Term
from ddq.topics.logics.logic import Function as LogicalFunction 
from ddq.util.check_type import check_type


class InductiveFormationFormulator(Formulator):
    def symbol(self) -> str:
        pass
    
    def __call__(self, *parameters) -> Node:
        return InductiveFormation(*parameters)
    
    
class InductiveFormation(LogicalFunction):
    def __init__(self, *in_children):
        super().__init__()
        self.set_children(in_children)
        
    def accepts_child(self, index: int, child: "Node") -> bool:
        return check_type(child, Term)
        
    @staticmethod
    def symbol() -> str:
        return "{}"
    
    def repr_node(self) -> NodeRepr:
        return self.symbol()