import copy
from typing import Set
from .node import Node


class Namer:
    def __init__(self):
        self._name_dict = {}
        self._first_name_candidates = ['x', 'y', 'z', 'w']

    def _new_name(self, taken_names: Set[str]) -> str:
        def make_name(prefix, index):
            return '{}_{}'.format(name, index)

        for cand in self._first_name_candidates:
            if cand not in taken_names:
                return cand
        for cand in self._first_name_candidates:
            for index in range(1, 3):
                name = make_name(name, index)
                if name not in taken_names:
                    return cand
        index = 4
        prefix = self._first_name_candidates[0]
        name = make_name(prefix, index)
        while name in taken_names:
            index = index + 1
            name = make_name(prefix, index)
        return name

    def _name_node(self, node: Node, taken_names: Set[str]) -> str:
        if isinstance(node.repr_node(), int):
            # We only need to name nodes that return the object id
            # as their representation. This is a convention.
            return self._new_name(taken_names)
        else:
            return None

    def analyze(self, node: Node):
        def recurse_analyze(node, parent_names: Set[str]):
            if node is None:
                return
            new_node_name = self._name_node(node, parent_names)
            if new_node_name is None:
                recurse_set = parent_names
            else:
                recurse_set = copy.copy(parent_names)
                recurse_set.add(new_node_name)
                self._name_dict[node] = new_node_name
            for child in node.children():
                recurse_analyze(child, recurse_set)
        recurse_analyze(node, set())

    def repr_node(self, node: Node) -> str:
        if node is None:
            return "None"
        return (self._name_dict[node]
                if node in self._name_dict
                else node.repr_node())
