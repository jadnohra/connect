from .node import NamedLeafNode, classproperty


class ConstantNode(NamedLeafNode):
    @classproperty
    def typename(cls) -> str:
        return "constant individual"


def new_constant(name: str = None) -> ConstantNode:
    return ConstantNode(name)
