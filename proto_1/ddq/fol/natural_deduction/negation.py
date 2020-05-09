from ddq.fol.connective import Connective, ConnectiveNode


class Not(Connective):
    def __init__(self):
        super().__init__('¬', 1, NotNode)


class NotNode(ConnectiveNode):
    pass


def l_not() -> NotNode:
    return Not().new_node()
