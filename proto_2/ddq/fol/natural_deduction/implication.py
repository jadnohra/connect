from ddq.fol.connective import Connective, ConnectiveNode


class Implication(Connective):
    def __init__(self):
        super().__init__('⇒', 2, ImplicationNode)


class ImplicationNode(ConnectiveNode):
    pass
