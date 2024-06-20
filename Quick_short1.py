def Quick_short(H):
    if len(H)<= 1:
        return H
    else:
        temp = H[0]
        grater = [x for x in H[1:]  if x >= temp]
        lessler = [x for x in H[1:] if x < temp]
        return Quick_short(lessler) + [temp] +  Quick_short(grater)


arr = [15, 30, 25, 69, 83, 57, 79, 99, 36, 1, 2]
Quick_short(arr)
print(arr)