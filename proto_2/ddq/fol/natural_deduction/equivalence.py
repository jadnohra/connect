from ddq.fol.connective import Connective, ConnectiveNode


class Equivalence(Connective):
    def __init__(self):
        super().__init__('⇔', 2, EquivalenceNode)


class EquivalenceNode(ConnectiveNode):
    pass
