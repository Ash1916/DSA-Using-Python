
#priourty Queue is list of tuples
class PriorityQueue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item)== 0
    
    def push(self, data, priority):
        index = 0
        while index < len(self.item) and self.item[index][1] <= priority:
            index += 1
        self.item.insert(index, (data, priority))
        
    def Pop(self):
        if self.is_empty():
            raise IndexError("Priourty Queue is Empty")
        return self.item.pop(0)[0]
    def size(self):
        return len(self.item)
    
    
p=PriorityQueue()
p.push("Aakash", 5)
p.push("Mohan", 8)
p.push("Rahul", 4)
p.push("Hitesh", 1)
p.push("hol", 0)
p.push("balck", 5)

while not p.is_empty():
    print(p.Pop())