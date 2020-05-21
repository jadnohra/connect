from typing import List
from ddq.taxonomy.reference import Reference
from ddq.taxonomy.node import Node, NodeRepr
from ddq.topics.logics.logic import Meta, Formulator, Function, Predicate
from ddq.util.check_type import check_type


class PredicativeFunctionDefinitionFormulator(Formulator):
    def info(self) -> str:
        return ("Definition sugar for functions that can be "
                "defined using a predicate")

    def references(self) -> List[Reference]:
        return [
            Reference(
                        "Type Theory and Formal Proof", 
                        [
                            ("Rob", "Schechter"), 
                            ("Herman", "Nederpelt")
                        ],
                        [
                            "p.172"
                        ]
                    )
            # and EST p.10
        ]

    def __call__(self, *parameters) -> Node:
        return PredicativeFunctionDefinition(*parameters)


class PredicativeFunctionDefinition(Meta):
    def __init__(self, *in_children):
        super().__init__()
        children = [Function, Predicate]
        for i in range(len(children)):
            if i < len(in_children):
                children[i] = in_children[i]
        self.set_children(children)
        
    def accepts_child(self, index: int, child: "Node") -> bool:
        type_checks = {0: Function, 1: Predicate}
        return check_type(child, type_checks[index])
    
    @staticmethod
    def symbol() -> str:
        return "≜"
    
    def repr_node(self) -> NodeRepr:
        return self.symbol()
    