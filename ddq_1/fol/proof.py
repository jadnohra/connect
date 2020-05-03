from .node import Node


class ProofNode(Node):
    def __init__(self):
        pass

    def is_leaf(self) -> bool:
        """True if this node is a leaf"""
        return self.children() is None

    def children(self) -> List["Node"]:
        """Returns a list of children. 
           Returning None is not equivalents to returning an empty array. 
           It signifies that this is a leaf node, as a opposed to a non-leaf
           node which happens to have no children."""
        pass

    def name(self) -> str:
        pass