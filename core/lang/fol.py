from typing import List


class PrimitiveSymbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def symbol_type(self) -> str:
        return 'primitive symbol'

    @staticmethod
    def new_symbol(symbol: str) -> "PrimitiveSymbol":
        return PrimitiveSymbol(symbol)

    def expression(self) -> str:
        return self.symbol

    def equals(self, other: "PrimitiveSymbol") -> bool:
        return type(self) == type(other) and self.symbol == other.symbol


class ImproperSymbol(PrimitiveSymbol):
    def symbol_type(self) -> str:
        return 'improper symbol'


class LeftParenSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('(')

    def symbol_type(self) -> str:
        return 'left parenthesis'

    @staticmethod
    def new() -> "LeftParenSymbol":
        return LeftParenSymbol()


class RightParenSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__(')')

    def symbol_type(self) -> str:
        return 'right parenthesis'

    @staticmethod
    def new() -> "RightParenSymbol":
        return RightParenSymbol()


class ConjSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('^')

    def symbol_type(self) -> str:
        return 'conjunction'

    @staticmethod
    def new() -> "ConjSymbol":
        return ConjSymbol()


class DisjSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('v')

    def symbol_type(self) -> str:
        return 'disjunction'

    @staticmethod
    def new() -> "DisjSymbol":
        return DisjSymbol()


class NegSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('~')

    def symbol_type(self) -> str:
        return 'negation'

    @staticmethod
    def new() -> "NegSymbol":
        return NegSymbol()


class ImplSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('=>')

    def symbol_type(self) -> str:
        return 'material implication'

    @staticmethod
    def new() -> "ImplSymbol":
        return ImplSymbol()


class EquivSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('==')

    def symbol_type(self) -> str:
        return 'material equivalence'

    @staticmethod
    def new() -> "EquivSymbol":
        return EquivSymbol()


class UniversalSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('∀')

    def symbol_type(self) -> str:
        return 'universal quantifier'

    @staticmethod
    def new() -> "UniversalSymbol":
        return UniversalSymbol()


class ExistentialSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('∃')

    def symbol_type(self) -> str:
        return 'existential quantifier'

    @staticmethod
    def new() -> "ExistentialSymbol":
        return ExistentialSymbol()


class Thing(PrimitiveSymbol):
    def __init__(self, name: str):
        PrimitiveSymbol.__init__(name)


class Constant(Thing):
    def __init__(self, name: str):
        Thing.__init__(name)

    def symbol_type(self) -> str:
        return 'constant'

    @staticmethod
    def new(name: str) -> "Constant":
        return Constant(name)


class Variable(Thing):
    def __init__(self, name: str):
        Thing.__init__(name)


class IndividualVariable(Variable):
    def __init__(self, name: str):
        Variable.__init__(name)

    def symbol_type(self) -> str:
        return 'individual variable'

    @staticmethod
    def new(name: str) -> "IndividualVariable":
        return IndividualVariable(name)


class PropositionalVariable(Variable):
    def __init__(self, name: str):
        Variable.__init__(name)

    def symbol_type(self) -> str:
        return 'propositional variable'

    @staticmethod
    def new(name: str) -> "PropositionalVariable":
        return PropositionalVariable(name)


class Function(PrimitiveSymbol):
    def __init__(self, name: str, arity: int):
        PrimitiveSymbol.__init__(name)
        self.arity = arity

    def symbol_type(self) -> str:
        return 'function'

    @staticmethod
    def new(name: str, arity: int) -> "Function":
        return Function(name, arity)


class Predicate(PrimitiveSymbol):
    def __init__(self, name: str, arity: int):
        PrimitiveSymbol.__init__(name)
        self.arity = arity

    def symbol_type(self) -> str:
        return 'function'

    @staticmethod
    def new(name: str, arity: int) -> "Predicate":
        return Predicate(name, arity)

'''
class Formula:
    def __init__(self, symbols: List[PrimitiveSymbol]):
        self.symbols =  symbols

    def symbol_type(self) -> str:
        return 'formula'

    @staticmethod
    def new(symbols: List[PrimitiveSymbol]) -> "Variable":
        return Formula(symbols)
'''


class Term:
    def __init__(self, atoms: List[PrimitiveSymbol]):
        self.atoms = atoms

    @staticmethod
    def new_thing(thing: Thing) -> "Term":
        return Term([thing])

    @staticmethod
    def new_function(function: Function, terms: List["Term"]) -> "Term":
        return Term([function] + terms)


class Wff(Term):
    def __init__(self, atoms: List[PrimitiveSymbol]):
        self.atoms = atoms

    def is_bound(self, var: IndividualVariable) -> bool:
        pass


class VarWff(Wff):
    @staticmethod
    def new(var: PropositionalVariable) -> "VarWff":
        return VarWff([var])

    def is_bound(self, var: IndividualVariable) -> bool:
        return False


class PredicateWff(Wff):
    @staticmethod
    def new(predicate: Predicate, terms: List[Term]) -> "PredicateWff":
        return Term([predicate] + terms)

    def is_bound(self, var: IndividualVariable) -> bool:
        return False


class NegWff(Wff):
    @staticmethod
    def new(wff: "Wff") -> "NegWff":
        return Wff([NegSymbol.new(), wff])

    def is_bound(self, var: IndividualVariable) -> bool:
        return self.symbols[1].is_bound(var)


class BinaryWff(Wff):
    @staticmethod
    def new(left: "Wff", middle: ImproperSymbol, right: "Wff") -> "BinaryWff":
        return Wff([LeftParenSymbol.new(), 
                    left, middle, right,
                    RightParenSymbol.new()])

    def is_bound(self, var: IndividualVariable) -> bool:
        return any(self.symbols[i].is_bound(var) for i in [0, 2])

    @staticmethod
    def new_conj(left: "Wff", right: "Wff") -> "BinaryWff":
        return Wff.new_binary(left, ConjSymbol.new(), right)

    @staticmethod
    def new_disj(left: "Wff", right: "Wff") -> "BinaryWff":
        return Wff.new_binary(left, DisjSymbol.new(), right)

    @staticmethod
    def new_impl(left: "Wff", right: "Wff") -> "BinaryWff":
        return Wff.new_binary(left, ImplSymbol.new(), right)

    @staticmethod
    def new_equiv(left: "Wff", right: "Wff") -> "BinaryWff":
        return Wff.new_binary(left, EquivSymbol.new(), right)


class QuantifierWff(Wff):
    @staticmethod
    def new(quant: ImproperSymbol, indiv_var: IndividualVariable, wff: "Wff"
            ) -> "QuantifierWff":
        return Wff.new_binary([quant, indiv_var, wff])

    def is_bound(self, var: IndividualVariable) -> bool:
        return self.symbols[1].equals(var) or self.symbols[2].is_bound(var)

    @staticmethod
    def new_universal(indiv_var: IndividualVariable, wff: "Wff"
                      ) -> "QuantifierWff":
        return Wff.new_binary([UniversalSymbol.new(), indiv_var, wff])

    @staticmethod
    def new_existential(indiv_var: IndividualVariable, wff: "Wff"
                        ) -> "QuantifierWff":
        return Wff.new_binary([ExistentialSymbol.new(), indiv_var, wff])

# TBC
# An Introduction to Mathematical Logic and Type Theory, Andrews p.46