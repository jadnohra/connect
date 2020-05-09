from ddq.fol.predicate import Predicate


class Membership(Predicate):
    def __init__(self):
        super().__init__('∈', 2)


def st_in() -> Membership:
    return Membership()
