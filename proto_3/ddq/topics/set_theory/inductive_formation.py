from ddq.topics.logics.logic import Formulator, Node, FunctionLike


class InductiveFormationFormulator(Formulator):
    def symbol(self) -> str:
        pass
    
    def __call__(self, *parameters) -> Node:
        pass
    
    
class InductiveFormation(FunctionLike):
    def __init__(self, *in_children):
        super().__init__()
        children = [Set, Set]
        for i in range(len(children)):
            if i < len(in_children):
                children[i] = in_children[i]
        self.set_children(children)
        
    @staticmethod
    def symbol() -> str:
        return "≜"
    
    def repr_node(self) -> NodeRepr:
        return self.symbol()