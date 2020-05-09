from ddq.fol.constant import Constant


class EmptySet(Constant):
    def __init__(self):
        super().__init__("∅")
