from ddq.fol.connective import Connective, ConnectiveNode


class Equivalent(Connective):
    def __init__(self):
        super().__init__('⇔', 2, EquivalentNode)


class EquivalentNode(ConnectiveNode):
    pass


def l_equiv() -> EquivalentNode:
    return Equivalent().new_node()
