from ddq.fol.constant import Constant
from ddq.fol.quantifier import (
    UniversalQuantifierNode, 
    ExistentialQuantifierNode)


class EmptySetConstant(Constant):
    def __init__(self):
        super().__init__("∅")


class EmptySetAxiom(Formula):
    def __init__(self, empty_set_constant: EmptySetConstant):
        # TODO build self
        #(UniversalQuantifierNode()
        #    .set_left(1))