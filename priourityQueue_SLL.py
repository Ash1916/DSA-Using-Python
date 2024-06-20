class Node:
    def __init__(self, data=None, priourity=None, next = None):
        self.data = data
        self.priourity = priourity
        self.next = next
        
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.count_item = 0
        
    def is_empty(self):
        return self.start is None
    
    def push(self, data, priourity):
        n = Node(data, priourity)
        '''
        if self.is_empty():
            self.start = n
        '''
        if not self.start or self.start.priourity > priourity:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priourity <= priourity:
                temp = temp.next
            n.next = temp.next
            temp.next = n
            
        self.count_item += 1
            
    def pop(self):
        if self.is_empty():
            return IndexError("Priourity is empty")
        else:
            v = self.start.data
            self.start = self.start.next
            self.count_item -= 1
            return v
    def size(self):
        return self.count_item
    
    
p=PriorityQueue()
p.push("Aakash", 5)
p.push("Mohan", 8)
p.push("Rahul", 4)
p.push("Hitesh", 1)
p.push("hol", 0)
p.push("balck", 5)

while not p.is_empty():
    print(p.pop())
        
        
        