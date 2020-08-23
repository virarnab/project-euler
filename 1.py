def div3(n):
    if n%3 == 0:
        return True
    else:
        return False
def div5(n):
    if n%5 == 0:
        return True
    else:
        return False
def div15(n):
    if n%15 == 0:
        return True
    else:
        return False
c = 0
for i in range (1,1000):
    if div3(i):
        c+=i 
    elif div5(i):
        c+=i 
    elif div15(i):
        c = c - i
    else:
        continue 
print(c)
