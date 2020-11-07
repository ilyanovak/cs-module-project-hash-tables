"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

from itertools import product
from pprint import pprint

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

combs = list(product(q, repeat=4))
calcs = {}

for comb in combs:
    f_a, f_b, f_c, f_d = f(comb[0]), f(comb[1]), f(comb[2]), f(comb[3]),
    if f_a + f_b == f_c - f_d:
        key = f'f({comb[0]}) + f({comb[1]}) = f({comb[2]}) - f({comb[3]})'
        value = f'{f_a} + {f_b} = {f_c} - {f_d}'
        calcs[key] = value

pprint(calcs)
