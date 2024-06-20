def merge_short(H):
    if len(H)>1:
        k = (len(H))// 2
        H1 = H[:k]
        H2 = H[k:]
        merge_short(H1)
        merge_short(H2)
        i = j = l = 0
        while i< len(H1) and j < len(H2):
            if H1[i] < H2[j]:
                H[l] = H1[i]
                i += 1
            else:
                H[l] = H2[j]
                j+= 1
            l += 1
        while i< len(H1):
            H[l] = H1[i]
            i += 1
            l += 1
        while j< len(H2):
            H[l] = H2[j]
            j += 1
            l += 1
        
arr = [15, 30, 25, 69, 83, 57, 79, 99, 36, 1, 2]
merge_short(arr)
print(arr)
                
    