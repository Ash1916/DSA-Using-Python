class HeapShort:
    def __init__(self):
        self.heap = []
        
    def Heap_str(self, H):
        for e in H:
            self.inseart(e)
    def inseart(self, ele):
        H = self.heap
        index = len(self.heap)
        U = (index - 1)//2
        while U > 0 and H[U] < ele:
            if index == len(self.heap):
                H.append(H[U])
            else:
                H[index] = H[U]
            index = U
            U = (index - 1)// 2
        if index == len(H):
            H.append(ele)
        else: 
            self.heap[index]=self.heap[U] 
            index=U 
            U=(index-1)//2
            
    def top(self):
        if len(self.heap)==0: 
            raise EmptyHeapException() 
        return self.heap[0] 
    def delete(self): #q6 
        if len(self.heap)==0: 
            raise EmptyHeapException() 
        if len(self.heap)==1: 
            return self.heap.pop() 
        max_value=self.heap[0] 
        temp=self.heap.pop() 
        index=0 
        leftChildIndex=2*index+1 
        rightChildIndex=2*index+2 
        
        while leftChildIndex<len(self.heap): 
            if rightChildIndex<len(self.heap): 
                if self.heap[leftChildIndex]>self.heap[rightChildIndex]: 
                    if self.heap[leftChildIndex]>temp: 
                        self.heap[index]=self.heap[leftChildIndex] 
                        index=leftChildIndex 
                    else: 
                        break 
                else: 
                    if self.heap[rightChildIndex]>temp: 
                        self.heap[index]=self.heap[rightChildIndex] 
                        index=rightChildIndex 
                    else: 
                        break 
            else: #NO RIGHT CHILD 
                if self.heap[leftChildIndex]>temp: 
                    self.heap[index]=self.heap[leftChildIndex] 
                    index=leftChildIndex 
                else: 
                    break
            leftChildIndex=2*index+1 
            rightChildIndex=2*index+2 
        self.heap[index]=temp 
        return max_value
    def heapSort(self,list1): #q7 
        self.Heap_str(list1) 
        list2=[] 
        try: 
            while True: 
                list2.insert(0,self.delete()) 
        except EmptyHeapException: 
            pass 
        return list2 
        
class EmptyHeapException(Exception): #q5 
    def __init__(self,msg="Empty Heap"): 
        self.msg=msg 
    def __str__(self):
        return self.msg
    
lis = [15, 30,25,69,83,57,79,99,36,1,2]
J = HeapShort()
k = J.heapSort(lis)
print(k)