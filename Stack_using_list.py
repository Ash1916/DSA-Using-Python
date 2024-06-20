class Stack:
    def __init__(self):
        self.item = []
        
    def is_empty(self):
        return len(self.item) == 0
    
    def push(self, data):
        self.item.append(data)
        return self.item
    def pop(self):
        if self.item is not None:
            self.item.pop()
            return self.item[-1]
        else:
            raise IndexError("list is empty")
    def peek(self):
        if self.item is not None:
            return self.item[-1]
        else:
            raise IndexError("List is empty")
    def size(self):
        if self.item is not None:
            return len(self.item)
        else:
            raise IndexError("list is empty")
        
        
        
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.pop()
k = s1.size()
print(k)
        
    