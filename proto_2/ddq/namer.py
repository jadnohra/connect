import copy
from typing import Set, Any
from .node import Node
from .fol.node_types import is_variable_declaration


class Namer:
    def __init__(self, name_id_representations = True):
        self._name_dict = {}
        self._first_name_candidates = ['t', 'u', 'v', 'x', 'y', 'z', 'w']
        self._name_id_representations = name_id_representations

    def _new_name(self, taken_names: Set[str]) -> str:
        def make_name(prefix, index):
            return '{}_{}'.format(prefix, index)

        for cand in self._first_name_candidates:
            if cand not in taken_names:
                return cand
        for cand in self._first_name_candidates:
            for index in range(1, 3):
                name = make_name(cand, index)
                if name not in taken_names:
                    return name
        index = 4
        prefix = self._first_name_candidates[0]
        name = make_name(prefix, index)
        while name in taken_names:
            index = index + 1
            name = make_name(prefix, index)
        return name

    def _name_node(self, node: Node, taken_names: Set[str]) -> str:
        if (self._name_id_representations and 
            isinstance(self.repr_node(node), int)):
            # We only need to name nodes that return the object id
            # as their representation. This is a convention.
            return self._new_name(taken_names)
        else:
            return None

    def analyze(self, node: Node):
        def recurse_analyze(node, taken_names: Set[str]):
            if node is None:
                return
            new_node_name = self._name_node(node, taken_names)
            if new_node_name is not None:
                taken_names.add(new_node_name)
                self._name_dict[node] = new_node_name
            decl_children = [x for x in node.children()
                             if is_variable_declaration(x)]
            nondecl_children = [x for x in node.children()
                                if not is_variable_declaration(x)]
            # Variable declarations as our children affect the names
            # of our other children, so we pass in taken_names by
            # reference, so that the declared names are added to it
            for child in decl_children:
                recurse_analyze(child, taken_names)
            for child in nondecl_children:
                recurse_analyze(child, copy.copy(taken_names))
        recurse_analyze(node, set())

    def _repr_resolve(self, thing: Any) -> str:
        if thing is None:
            # Support None gracefully
            return "None"
        if not isinstance(thing, Node):
            # If we have a string or an int return them
            # This complication is needed to handle Node.repr_node
            # returing a reference node.
            return thing
        else:
            node = thing
            return (self._name_dict[node]
                    if node in self._name_dict
                    else self._repr_resolve(node.repr_node()))

    def repr_node(self, node: Node) -> str:
        return self._repr_resolve(node)
