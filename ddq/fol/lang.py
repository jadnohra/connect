'''
References:
 - An Introduction to Mathematical Logic and Type Theory, Andrews p.46
'''

from typing import List, Tuple

class Node:
    def is_leaf(self) -> bool:
        return self.children() is None

    def children(self) -> List["Node"]:
        pass

    def name(self) -> str:
        pass

class Symbol(Node):
    def __init__(self):
        pass

    def symbol_type(self) -> str:
        return 'symbol'

    def expression(self) -> str:
        return ''

    def children(self) -> List["Node"]:
        return None

    def name(self) -> str:
        return self.expression()

    @staticmethod
    def canonical_instance() -> "Symbol":
        return Symbol()

class PrimitiveSymbol(Symbol):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol

    def symbol_type(self) -> str:
        return 'primitive symbol'

    def expression(self) -> str:
        return self.symbol

    def equals(self, other: "PrimitiveSymbol") -> bool:
        return type(self) == type(other) and self.symbol == other.symbol

    @staticmethod
    def canonical_instance() -> "PrimitiveSymbol":
        return PrimitiveSymbol('?')

class ImproperSymbol(PrimitiveSymbol):
    def symbol_type(self) -> str:
        return 'improper symbol'

    @staticmethod
    def canonical_instance() -> "ImproperSymbol":
        return ImproperSymbol('?')


class LeftParenSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('(')

    def symbol_type(self) -> str:
        return 'left parenthesis'

    @staticmethod
    def canonical_instance() -> "LeftParenSymbol":
        return LeftParenSymbol()


class RightParenSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__(')')

    def symbol_type(self) -> str:
        return 'right parenthesis'

    @staticmethod
    def canonical_instance() -> "RightParenSymbol":
        return RightParenSymbol()


class ConjSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('^')

    def symbol_type(self) -> str:
        return 'conjunction'

    @staticmethod
    def canonical_instance() -> "ConjSymbol":
        return ConjSymbol()


class DisjSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('v')

    def symbol_type(self) -> str:
        return 'disjunction'

    @staticmethod
    def canonical_instance() -> "DisjSymbol":
        return DisjSymbol()


class NegSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('~')

    def symbol_type(self) -> str:
        return 'negation'

    @staticmethod
    def canonical_instance() -> "NegSymbol":
        return NegSymbol()


class ImplSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('=>')

    def symbol_type(self) -> str:
        return 'material implication'

    @staticmethod
    def canonical_instance() -> "ImplSymbol":
        return ImplSymbol()


class EquivSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('==')

    def symbol_type(self) -> str:
        return 'material equivalence'

    @staticmethod
    def canonical_instance() -> "EquivSymbol":
        return EquivSymbol()


class UniversalSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('∀')

    def symbol_type(self) -> str:
        return 'universal quantifier'
    
    @staticmethod
    def canonical_instance() -> "UniversalSymbol":
        return UniversalSymbol()


class ExistentialSymbol(ImproperSymbol):
    def __init__(self):
        super().__init__('∃')

    def symbol_type(self) -> str:
        return 'existential quantifier'

    @staticmethod
    def canonical_instance() -> "ExistentialSymbol":
        return ExistentialSymbol()


class IndividualSymbol(PrimitiveSymbol):
    def __init__(self, name: str):
        super().__init__(name)

    def symbol_type(self) -> str:
        return 'individual'

    @staticmethod
    def canonical_instance() -> "IndividualSymbol":
        return IndividualSymbol('?')


class Constant(IndividualSymbol):
    def __init__(self, name: str):
        super().__init__(name)

    def symbol_type(self) -> str:
        return 'constant'

    @staticmethod
    def canonical_instance() -> "Constant":
        return Constant('c')


class Variable(IndividualSymbol):
    def __init__(self, name: str):
        super().__init__(name)

    def symbol_type(self) -> str:
        return 'variable'

    @staticmethod
    def canonical_instance() -> "Variable":
        return Variable('?')


class IndividualVariable(Variable):
    def __init__(self, name: str):
        super().__init__(name)

    def symbol_type(self) -> str:
        return 'individual variable'

    @staticmethod
    def canonical_instance() -> "IndividualVariable":
        return IndividualVariable('p')


class PropositionalVariable(Variable):
    def __init__(self, name: str):
        super().__init__(name)

    def symbol_type(self) -> str:
        return 'propositional variable'

    @staticmethod
    def canonical_instance() -> "PropositionalVariable":
        return PropositionalVariable('X')


class Function(PrimitiveSymbol):
    def __init__(self, name: str, arity: int):
        super().__init__(name)
        self.arity = arity

    def symbol_type(self) -> str:
        return 'function'

    @staticmethod
    def canonical_instance() -> "Function":
        return Function('f', 1)


class Predicate(PrimitiveSymbol):
    def __init__(self, name: str, arity: int):
        super().__init__(name)
        self.arity = arity

    def symbol_type(self) -> str:
        return 'predicate'

    @staticmethod
    def canonical_instance() -> "Predicate":
        return Predicate('P', 1)


class Term(Node):
    def __init__(self, atoms: List[PrimitiveSymbol]):
        self.atoms = atoms

    def get_vars(self) -> List[Variable]:
        return [x for x in self.atoms if isinstance(x, Variable)]

    def expression(self) -> str:
        return "".join(atom.expression() for atom in self.atoms)

    def children(self) -> List["Node"]:
        return self.atoms

    def name(self) -> str:
        return "Term"

    @staticmethod
    def canonical_instance() -> "Term":
        return Term([IndividualSymbol.canonical_instance()])


class ConstantTerm(Term):
    def __init__(self, constant: Constant):
        super().__init__([constant])

    def name(self) -> str:
        return "Constant Term"

    @staticmethod
    def canonical_instance() -> "ConstantTerm":
        return ConstantTerm(Constant.canonical_instance())


class IndivVarTerm(Term):
    def __init__(self, var: IndividualVariable):
        super().__init__([var])

    def name(self) -> str:
        return "Individual Variable Term"

    @staticmethod
    def canonical_instance() -> "IndivVarTerm":
        return IndivVarTerm(IndividualVariable.canonical_instance())



class FunctionTerm(Term):
    def __init__(self, function: Function, terms: List["Term"]):
        super().__init__([function] + terms)

    def name(self) -> str:
        return "Function Term"

    @staticmethod
    def canonical_instance() -> "FunctionTerm":
        return FunctionTerm(Function.canonical_instance(),
                            [IndivVarTerm.canonical_instance()])


class Wff(Node):
    def __init__(self, symbols: List[PrimitiveSymbol]):
        self.symbols = symbols

    def is_atomic(self) -> bool:
        pass

    def get_bound_vars(self) -> List[Tuple["Wff", IndividualVariable]]:
        pass

    def get_free_vars(self) -> List[IndividualVariable]:
        pass

    def substitute(self):  # TODO Andrews p.49
        pass

    def is_bound(self, var: IndividualVariable) -> bool:
        return any(var == x for (x, y) in self.get_bound_vars())

    def is_closed(self) -> bool:
        return len([x for x in self.get_free_vars()
                    if isinstance(x, IndividualVariable)]) == 0

    def is_sentence(self) -> bool:
        return len(self.get_free_vars()) == 0

    def expression(self) -> str:
        return "".join(symbol.expression() for symbol in self.symbols)

    def children(self) -> List["Node"]:
        return self.symbols

    def name(self) -> str:
        return "Wff"

    @staticmethod
    def canonical_instance() -> "Wff":
        return Wff([Constant.canonical_instance()])


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

    def name(self) -> str:
        return "Propositional Variable Wff"

    @staticmethod
    def canonical_instance() -> "PropVarWff":
        return PropVarWff([PropositionalVariable.canonical_instance()])


class PredicateWff(Wff):
    def __init__(self, predicate: Predicate, terms: List[Term]):
        super.__init__([predicate] + terms)

    def is_atomic(self) -> bool:
        return True

    def is_bound(self, var: IndividualVariable) -> bool:
        return False

    def get_bound(self) -> List[Tuple["Wff", IndividualVariable]]:
        return []

    def get_free(self) -> List[IndividualVariable]:
        return sum([x.get_vars() for x in self.symbols[1:]], [])

    def name(self) -> str:
        return "Predicate Wff"

    @staticmethod
    def canonical_instance() -> "PredicateWff":
        return PredicateWff(Predicate.canonical_instance(), 
                            [IndividualVariable.canonical_instance()])


class NegWff(Wff):
    def __init__(self, wff: "Wff"):
        super().__init__([NegSymbol(), wff])

    def is_atomic(self) -> bool:
        return False

    def is_bound(self, var: IndividualVariable) -> bool:
        return self.symbols[1].is_bound(var)

    def get_bound(self) -> List[Tuple["Wff", IndividualVariable]]:
        return self.symbols[1].get_bound()

    def get_free(self) -> List[IndividualVariable]:
        return self.symbols[1].get_free()

    def name(self) -> str:
        return "Negation Wff"


class BinaryWff(Wff):
    def __init__(self, left: "Wff", middle: ImproperSymbol, right: "Wff"):
        super().__init__(
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

    def name(self) -> str:
        return "Binary Wff"


class ConjWff(BinaryWff):
    def __init__(self, left: "Wff", right: "Wff"):
        super().__init__(left, ConjSymbol(), right)

    def name(self) -> str:
        return "Conjunction Wff"


class DisjWff(BinaryWff):
    def __init__(self, left: "Wff", right: "Wff"):
        super().__init__(left, DisjSymbol(), right)

    def name(self) -> str:
        return "Disjunction Wff"


class ImplWff(BinaryWff):
    def __init__(self, left: "Wff", right: "Wff"):
        super().__init__(left, ImplSymbol(), right)

    def name(self) -> str:
        return "Implication Wff"


class EquivWff(BinaryWff):
    def __init__(self, left: "Wff", right: "Wff"):
        super().__init__(left, EquivSymbol(), right)

    def name(self) -> str:
        return "Equivalence Wff"


class QuantifierWff(Wff):
    def __init__(self, quant: ImproperSymbol, indiv_var: IndividualVariable, wff: "Wff"
                 ):
        Wff([quant, indiv_var, wff])

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

    def name(self) -> str:
        return "Quantifier Wff"


class UniversalWff(QuantifierWff):
    def __init__(self, indiv_var: IndividualVariable, wff: "Wff"):
        super().__init__(UniversalSymbol(), indiv_var, wff)

    def name(self) -> str:
        return "Universal Quantifier Wff"


class ExistentialWff(QuantifierWff):
    def __init__(self, indiv_var: IndividualVariable, wff: "Wff"):
        super().__init__(ExistentialSymbol(), indiv_var, wff)

    def name(self) -> str:
        return "Existenstial Quantifier Wff"
