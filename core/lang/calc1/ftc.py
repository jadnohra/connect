'''
References:
 - Type Theory and Formal Proof, Geuvers p.166, 169
'''
from core.lang.fol import lang

'''
31.1
premisses:
 - f integrable on [a, b]
 - F(x) := Integral(a,b,f) unif cont on [a,b]
 - f cont at c in [a,b]
conclusions
 - F diff at c
 - F'(c) = f(c)
'''

'''
integrable
29.3
pattern1:
 - f integrable on [a,b]
pattern2:
 - lower integral (a,b,f) = upper integral (a,b,f)
'''

'''
lower/upper integral
29.3
pattern1:
 - lower integral (a,b,f)
pattern2:
 - forall P : sup{L(f,P)}, {L(f,P)} := Lf ({partitions of P})
    - {partitions of P} :=
        - note: we never 'form these sets'
'''

'''
what is sup, a function R->R? a partial? function set of reals -> real
no sup is a logical function, introduced by a definition! and proven to be allowed by the properties of R
pattern1:
 - s = sup(A)?
 - sup(A)
pattern2:
 - (a in A => s >= a) ^ (m < s => exists a' in A a' > m)
'''

'''
definition of sup
context
 - A in in Pow(R)
 - bounded(A)
definition
 - definiendum
    - sup(A)
 - definiens
    - sup(A) in R
    - (a in A => sup(A) >= a) ^ (m < sup(A) => exists a' in A a' > m)


'''

'''
class Function:
    def get_parameters():
        pass
'''

Actually, we have a tree of contexts!
and our idea from connect somehow still applies

predicate real number
    axiomatic how?

predicate set of reals
    context:
        - A: set
    condition:
        - A subset Pow(R)

predicate bounded
    context:
        - A: set of reals
    condition:
        - exists M: forall a: a in A => a <= M


for all (sets A). A is bounded => sup(A) exists   BUT sup(A) was not defined, do we need a 'definition'? the function itself below is the definition! class SupFunction
 - actually not exists! but A is in the domain of sup!
for all (sets A). sup(A) exists => a in A => a <= sup(A)

class SupFunction(lang.FunctionTerm):
    def __init__(self):
        super().__init__(lang.Function('sup'), lang.IndivVarTerm(lang.IndividualVariable('A'))


class SupProperty1(lang.ImplWff):
    def __init__(self):
        super().__init__()
