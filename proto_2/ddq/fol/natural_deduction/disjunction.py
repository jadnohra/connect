from ddq.fol.connective import Connective, ConnectiveNode


class Disjunction(Connective):
    def __init__(self):
        super().__init__('∨', 2, DisjunctionNode)


class DisjunctionNode(ConnectiveNode):
    pass
