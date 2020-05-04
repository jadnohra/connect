from typing import Union


class Type:
    pass


class DiscourseType(Type):
    pass


class Term(DiscourseType):
    pass


class TruthValue(DiscourseType):
    pass


class TermTuple(Type):
    def __init__(self, arity: int):
        self._arity = arity

    def arity(self) -> int:
        return self._arity


class FunctionalType:
    def __init__(self,
                 to_type: Type,
                 from_type: Type = None):
        self._from_type = from_type
        self._to_type = to_type

    def from_type(self) -> Union[Type, None]:
        return self._from_type

    def to_type(self) -> Type:
        return self._to_type
