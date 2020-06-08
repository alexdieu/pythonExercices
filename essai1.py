import functools

# boucle while
def factorielle1(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

# recursif

def factorielle2(n):
    if n == 0:
        return 1
    else:
        return n * factorielle2(n-1)

# lambda + reduction

def factorielle3(n):
    f = lambda x,y:x*y
    l = list(range(1,n+1))
    return functools.reduce(f,l)


print(factorielle1(5))
print(factorielle1(5))
print(factorielle3(5))