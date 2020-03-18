class PrimitiveSymbol:
    def __init__(self):
        pass

class ImproperSymbol(PrimitiveSymbol):
    def __init__(self):
        pass

class ProperSymbol(PrimitiveSymbol):
    def __init__(self):
        pass

class PropVariable:
    def __init__(self):
        pass

class Formula:
    def __init__(self):
        pass


class Expr:
    def __init__(self):
        pass

class Prop(Expr):
    def __ini__(self):
        pass

class ModusPonens(Expr):
    def __init__(self, left: Prop, right: Prop):
        self.left = left
        self.right = right

class ModusTollens(Expr):
