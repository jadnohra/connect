from typing import List
from ddq.taxonomy.reference import Reference
from ddq.taxonomy.node import NodeRepr
from ddq.topics.logics.logic import Meta, Node, Formulator, Function, Predicate


class PredicativClassFunctionDefinition(Formulator):
    def info(self) -> str:
        return ("Definition sugar for class functions that can be"
                " defined using a predicate")

    def notes(self) -> List[str]:
        return ["The defined construct may look a like function, "
                "but may not formally be so, as its domain may be a "
                "proper class and not a set."]
    
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

    def symbol(self) -> str:
        return PredicativeClassFunctionDefinition.symbol()
    
    def __call__(self, *parameters) -> Node:
        self._shape = PredicativeClassFunctionDefinition(*parameters)


class PredicativeClassFunctionDefinition(Meta):
    def __init__(self, *in_children):
        children = [Function, Predicate]
        for i in range(len(children)):
            if i < len(children):
                children[i] = in_children[i]
        self.set_children(children)
        
    @staticmethod
    def symbol() -> str:
        return "≜"
    
    def repr_node(self) -> NodeRepr:
        return self.symbol()
    