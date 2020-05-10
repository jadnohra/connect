from ddq.fol.connective import Connective, ConnectiveNode


class Negation(Connective):
    def __init__(self):
        super().__init__('¬', 1, NegationNode)


class NegationNode(ConnectiveNode):
    pass
