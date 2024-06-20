M = [15, 30,25,69,83,57,79,99,36,1,2]
#n = 1
def double_short(H):
    for i in range(1, len(H)):
        for n in range(len(H)- i):
            if H[n] > H[n+1]:
                H[n], H[n+1] = H[n+1],H[n]
                
def modified_double_short(H):
    for i in range(1, len(H)):
        tag = False
        for n in range(len(H)- i):
            if H[n] > H[n+1]:
                H[n], H[n+1] = H[n+1],H[n]
        tag = True
        if not tag:
            break
    
modified_double_short(M)
print(M)