from ddq.fol.constant import Constant


class EmptySetConstant(Constant):
    def __init__(self):
        super().__init__("∅")


class EmptySetAxiom(Formula):
    def __init__(self, empty_set_constant: EmptySetConstant):
        TODO build self
