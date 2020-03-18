import typing
from typing import List


class PrimitiveSymbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def symbol_type(self) -> str:
        return 'primitive symbol'

    @staticmethod
    def new_symbol(symbol: str) -> "PrimitiveSymbol":
        return PrimitiveSymbol(symbol)

    def expression(self) -> self:
        return self.symbol
        

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
        PrimitiveSymbol.__init__('A')

    def symbol_type(self) -> str:
        return 'universal quantifier'

    @staticmethod
    def new() -> "UniversalSymbol":
        return UniversalSymbol()


class ExistentialSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('E')

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
        self.atoms =  atoms

    @staticmethod
    def new_thing(thing: Thing) -> "Term":
       return Term([thing])

    @staticmethod
    def new_function(function: Function, terms: List[Term]) -> "Term":
       return Term([function] + terms)


class Wff(Term):
    def __init__(self, atoms: List[PrimitiveSymbol]):
        self.atoms =  atoms

    @staticmethod
    def new_prop_var(var: PropositionalVariable) -> "Wff":
       return Wff([var])

    @staticmethod
    def new_predicate(predicate: Predicate, terms: List[Term]) -> "Wff":
       return Term([predicate] + terms)

    @staticmethod
    def new_neg(wff: "Wff") -> "Wff":
        return Wff([NegSymbol.new(), var])

    @staticmethod
    def new_binary(left: "Wff", middle: ImproperSymbol, right: "Wff") -> "Wff":
        return Wff([LeftParenSymbol.new(), 
                    left, middle, right,
                    RightParenSymbol.new()])

    @staticmethod
    def new_conj(left: "Wff", right: "Wff") -> "Wff":
        return new_binary(left, ConjSymbol.new(), right)

    @staticmethod
    def new_disj(left: "Wff", right: "Wff") -> "Wff":
        return new_binary(left, DisjSymbol.new(), right)

    @staticmethod
    def new_impl(left: "Wff", right: "Wff") -> "Wff":
        return new_binary(left, ImplSymbol.new(), right)

    @staticmethod
    def new_equiv(left: "Wff", right: "Wff") -> "Wff":
        return new_binary(left, EquivSymbol.new(), right)

    @staticmethod
    def new_universal(indiv_var: IndividualVariable, wff: "Wff") -> "Wff":
        return new_binary([UniversalSymbol.new(), indiv_var, wff])

    @staticmethod
    def new_existential(indiv_var: IndividualVariable, wff: "Wff") -> "Wff":
        return new_binary([ExistentialSymbol.new(), indiv_var, wff])

# TBC
# An Introduction to Mathematical Logic and Type Theory, Andrews p.46