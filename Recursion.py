def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=' ')
        
def printNReverse(n):
    if n > 0:
        print(n, end=' ')
        printN(n-1)
        
def printNoddnatural(n):
    if n > 0:
        printNoddnatural(n-1)
        print(2*n-1, end=' ')
        
def printNEvennatural(n):
    if n > 0:
        printNEvennatural(n-1)
        print(2*n, end=' ')
        
def printNoddnaturalRverse(n):
    if n > 0:
        print(2*n-1, end=' ')
        printNoddnaturalRverse(n-1)
        
        
def printNEvennaturalRverse(n):
    if n > 0:
        print(2*n, end=' ')
        printNEvennaturalRverse(n-1)
        
        
#printN(10)
#printNReverse(10)
#printNoddnatural(10)
#printNEvennatural(10)
#printNoddnaturalRverse(10)
printNEvennaturalRverse(10)
