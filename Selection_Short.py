lis = [15, 30,25,69,83,57,79,99,36,1,2]
def selection_short(H):
    n = len(lis)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
           if H[j] < H[min]:
               min = j
        H[i], H[min] = H[min], H[i]

selection_short(lis)
print(lis)
        
        