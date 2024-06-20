def printN(n):
    if n == 1:
        return 1
    k = n + printN(n-1)
    return k

def printNodd(n):
    if n == 1:
        return 1
    k = 2*n-1 + printNodd(n-1)
    return k
def printNEven(n):
    if n == 1:
        return 2
    k = 2*n + printNEven(n-1)
    return k

def printNFact(n):
    if n == 0:
        return 1
    k = n * printNFact(n-1)
    return k

def printNSqure(n):
    if n == 1:
        return 1
    k = n*n + printNSqure(n-1)
    return k
        
print(printNSqure(5))
