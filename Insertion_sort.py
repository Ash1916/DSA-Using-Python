def Insertion_short(H):
    for i in range(1, len(H)):
        temp = H[i]
        j = i-1
        while j >= 0 and temp < H[j]:
            H[j+1] = H[j]
            j -= 1
        H[j+1] = temp
        
lis = [15, 30,25,69,83,57,79,99,36,1,2]
Insertion_short(lis)
print(lis)