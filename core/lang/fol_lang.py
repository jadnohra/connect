'''
References:
 - An Introduction to Mathematical Logic and Type Theory, Andrews p.46
'''

from typing import List, Tuple


class PrimitiveSymbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def symbol_type(self) -> str:
        return 'primitive symbol'

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


class RightParenSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__(')')

    def symbol_type(self) -> str:
        return 'right parenthesis'


class ConjSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('^')

    def symbol_type(self) -> str:
        return 'conjunction'


class DisjSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('v')

    def symbol_type(self) -> str:
        return 'disjunction'


class NegSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('~')

    def symbol_type(self) -> str:
        return 'negation'


class ImplSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('=>')

    def symbol_type(self) -> str:
        return 'material implication'


class EquivSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('==')

    def symbol_type(self) -> str:
        return 'material equivalence'


class UniversalSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('∀')

    def symbol_type(self) -> str:
        return 'universal quantifier'


class ExistentialSymbol(ImproperSymbol):
    def __init__(self):
        PrimitiveSymbol.__init__('∃')

    def symbol_type(self) -> str:
        return 'existential quantifier'


class Constant(PrimitiveSymbol):
    def __init__(self, name: str):
        PrimitiveSymbol.__init__(name)

    def symbol_type(self) -> str:
        return 'constant'


class Variable(PrimitiveSymbol):
    def __init__(self, name: str):
        PrimitiveSymbol.__init__(name)


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


class Term:
    def __init__(self, atoms: List[PrimitiveSymbol]):
        self.atoms = atoms

    def get_vars(self) -> List[Variable]:
        return [x for x in self.atoms if isinstance(x, Variable)]


class ConstantTerm(Term):
    @staticmethod
    def new(constant: Constant) -> "ConstantTerm":
        return Term([constant])


class IndivVarTerm(Term):
    @staticmethod
    def new(var: IndividualVariable) -> "IndivVarTerm":
        return Term([var])


class FunctionTerm(Term):
    @staticmethod
    def new(function: Function, terms: List["Term"]) -> "Term":
        return Term([function] + terms)


class Wff:
    def __init__(self, symbols: List[PrimitiveSymbol]):
        self.symbols = symbols

    def is_atomic(self) -> bool:
        pass

    def get_bound_vars(self) -> List[Tuple["Wff", IndividualVariable]]:
        return []

    def get_free_vars(self) -> List[IndividualVariable]:
        return self.get_vars()

    def substitute(self):  # TODO Andrews p.49
        pass

    def is_bound(self, var: IndividualVariable) -> bool:
        return any(var == x for (x, y) in self.get_bound_vars())

    def is_closed(self) -> bool:
        return len([x for x in self.get_free_vars()
                    if isinstance(x, IndividualVariable)]) == 0

    def is_sentence(self) -> bool:
        return len(self.get_free_vars()) == 0


class PropVarWff(Wff):
    def __init__(self, var: PropositionalVariable):
        super.__init__([var])

    def is_atomic(self) -> bool:
        return True

    def is_bound(self, var: IndividualVariable) -> bool:
        return False

    def get_bound_vars(self) -> List[Tuple["Wff", IndividualVariable]]:
        return []

    def get_free_vars(self) -> List[IndividualVariable]:
        return self.symbols[0]


class PredicateWff(Wff):
    def __init__(self, predicate: Predicate, terms: List[Term]) -> "PredicateWff":
        return super.__init__([predicate] + terms)

    def is_atomic(self) -> bool:
        return True

    def is_bound(self, var: IndividualVariable) -> bool:
        return False

    def get_bound(self) -> List[Tuple["Wff", IndividualVariable]]:
        return []

    def get_free(self) -> List[IndividualVariable]:
        return sum([x.get_vars() for x in self.symbols[1:]], [])


class NegWff(Wff):
    def __init__(self, wff: "Wff"):
        return super().__init__([NegSymbol.new(), wff])

    def is_atomic(self) -> bool:
        return False

    def is_bound(self, var: IndividualVariable) -> bool:
        return self.symbols[1].is_bound(var)

    def get_bound(self) -> List[Tuple["Wff", IndividualVariable]]:
        return self.symbols[1].get_bound()

    def get_free(self) -> List[IndividualVariable]:
        return self.symbols[1].get_free()


class BinaryWff(Wff):
    def __init__(self, left: "Wff", middle: ImproperSymbol, right: "Wff"):
        return super().__init__(
                    [LeftParenSymbol(),
                     left, middle, right,
                     RightParenSymbol()])

    def is_atomic(self) -> bool:
        return False

    def is_bound(self, var: IndividualVariable) -> bool:
        return any(self.symbols[i].is_bound(var) for i in [0, 2])

    def get_bound(self) -> List[Tuple["Wff", IndividualVariable]]:
        return sum(self.symbols[i].get_bound() for i in [0, 2])

    def get_free(self) -> List[IndividualVariable]:
        return sum(self.symbols[i].get_free() for i in [0, 2])

    @staticmethod
    def new_conj(left: "Wff", right: "Wff") -> "BinaryWff":
        return BinaryWff(left, ConjSymbol.new(), right)

    @staticmethod
    def new_disj(left: "Wff", right: "Wff") -> "BinaryWff":
        return BinaryWff(left, DisjSymbol.new(), right)

    @staticmethod
    def new_impl(left: "Wff", right: "Wff") -> "BinaryWff":
        return BinaryWff(left, ImplSymbol.new(), right)

    @staticmethod
    def new_equiv(left: "Wff", right: "Wff") -> "BinaryWff":
        return BinaryWff(left, EquivSymbol.new(), right)


class QuantifierWff(Wff):
    def __init__(self, quant: ImproperSymbol, indiv_var: IndividualVariable, wff: "Wff"
                 ):
        return BinaryWff([quant, indiv_var, wff])

    def is_atomic(self) -> bool:
        return False

    def is_bound(self, var: IndividualVariable) -> bool:
        return self.symbols[1].equals(var) or self.symbols[2].is_bound(var)

    def get_bound(self) -> List[Tuple["Wff", IndividualVariable]]:
        return [(self, self.symbols[1])] + self.symbols[2].get_bound()

    def var(self) -> IndividualVariable:
        return self.symbols[1]

    def get_free(self) -> List[IndividualVariable]:
        free = self.symbols[2].get_free()
        if self.var() in free:
            free.remove(self.var())
        return free

    @staticmethod
    def new_universal(indiv_var: IndividualVariable, wff: "Wff"
                      ) -> "QuantifierWff":
        return Wff.new_binary([UniversalSymbol.new(), indiv_var, wff])

    @staticmethod
    def new_existential(indiv_var: IndividualVariable, wff: "Wff"
                        ) -> "QuantifierWff":
        return Wff.new_binary([ExistentialSymbol.new(), indiv_var, wff])
