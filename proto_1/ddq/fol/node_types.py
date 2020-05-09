from ddq.node import Node


def is_term(node: Node) -> bool:
    from .variable import VariableNode
    return isinstance(node, VariableNode)


def is_predicate(node: Node) -> bool:
    from .predicate import PredicateNode
    return isinstance(node, PredicateNode)


def is_connective(node: Node) -> bool:
    from .connective import ConnectiveNode
    return isinstance(node, ConnectiveNode)

def is_variable_declaration(node: Node) -> bool:
    from .variable import VariableDeclarationNode
    return isinstance(node, VariableDeclarationNode)
