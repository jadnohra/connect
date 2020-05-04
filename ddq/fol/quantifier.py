class BindContext:
    def __init__(self, parent: "BindContext" = None):
        self._parent = parent

    def new_variable(self) -> "BoundVariable":
        pass


class BoundVariable:
    def __init__(self):
        pass


class UniversalQuantifier(BindContext):
    def __init__(self, parent_context: BindContext = None):
        super().__init__(parent_context)
