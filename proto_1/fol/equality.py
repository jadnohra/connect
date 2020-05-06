from .predicate import Predicate


class Equality(Predicate):
    def __init__(self):
        super().__init__('=', 2)
