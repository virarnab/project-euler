import sympy
montu = [2]
montu_input = 1000000
#print(montu[-1])
test=1
while test<montu_input:
    l = 1
    for p in montu:
        l = l*p
    if l>montu_input:
        print(l/montu[-1])
        break
    else:
        montu.append(sympy.nextprime(montu[-1]))
