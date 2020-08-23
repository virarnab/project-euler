from sympy import sieve
g = [i for i in sieve.primerange(2, 2000000)]
c = 0
for x in g:
    c = c + x
print(c)
