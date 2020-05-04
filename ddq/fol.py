
class Predicate:
    def __init__(self, arity: int):
        self._arity = arity
        self._children = [None]*aritys