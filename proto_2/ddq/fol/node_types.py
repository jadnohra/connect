from ddq.node import Node


def is_variable(node: Node) -> bool:
    from .variable import VariableNode
    return isinstance(node, VariableNode)


def is_function(node: Node) -> bool:
    from .function import FunctionNode
    return isinstance(node, FunctionNode)


def is_term(node: Node) -> bool:
    return is_variable(node) or is_function(node)


def is_predicate(node: Node) -> bool:
    from .predicate import PredicateNode
    return isinstance(node, PredicateNode)


def is_connective(node: Node) -> bool:
    from .connective import ConnectiveNode
    return isinstance(node, ConnectiveNode)


def is_quantifier(node: Node) -> bool:
    from .quantifier import QuantifierNode
    return isinstance(node, QuantifierNode)


def is_variable_declaration(node: Node) -> bool:
    from .variable import VariableDeclarationNode
    return isinstance(node, VariableDeclarationNode)
