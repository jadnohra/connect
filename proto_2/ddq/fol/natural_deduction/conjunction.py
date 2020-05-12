from ddq.fol.connective import Connective, ConnectiveNode


class Conjunction(Connective):
    def __init__(self):
        super().__init__('∧', 2, ConjunctionNode)


class ConjunctionNode(ConnectiveNode):
    pass
