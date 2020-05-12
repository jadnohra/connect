from ddq.node import Node


def is_term(node: Node) -> bool:
    from .variable import VariableNode
    from .function import FunctionNode
    return any(isinstance(node, term_type) for term_type in
               [VariableNode, FunctionNode])


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
