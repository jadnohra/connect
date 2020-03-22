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