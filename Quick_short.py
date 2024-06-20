def Quick_short(self):
    
    pass
def Short(H):
    left = 0
    right = len(H)-1
    loc = 0
    for i in range(len(H)):
        if loc != left or loc != right:
            while H[loc] < H[right]:
                right -= 1
            H[loc], H[right] = H[right], H[loc]
            
            while H[loc] > H[left]:
                left += 1
            H[loc], H[left] = H[left], H[loc]
arr = [15, 30, 25, 69, 83, 57, 79, 99, 36, 1, 2]

Short(arr)
print(arr)
            
        
        
        
        