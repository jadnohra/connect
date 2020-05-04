from ddq.node import Node


class BindContext:
    def __init__(self):
        self._id_counter = 0

    def new_variable(self) -> "BoundVariable":
        yield BoundVariable(self._id_counter)
        self._id_counter = self._id_counter + 1


class BoundVariable:
    def __init__(self, id: int):
        self._id = id


class Quantifier(Node):
    def __init__(self, bind_context: BindContext = None):
        self._bind_context = (BindContext()
                              if bind_context is None
                              else bind_context)
        self._variable = self._bind_context.new_variable()

    def variable(self) -> BoundVariable:
        return self._variable

    def bind_context(self) -> BindContext:
        return self._bind_context

    ]def children(self) -> List:
        pass


class UniversalQuantifier(Quantifier):
    def __init__(self, bind_context: BindContext = None):
        super().__init__(bind_context)


class ExistentialQuantifier(Quantifier):
    def __init__(self, bind_context: BindContext = None):
        super().__init__(bind_context)

