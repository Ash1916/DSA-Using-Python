from SLL import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item = 0
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        self.insert_at_start(data)
        self.item += 1
        
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item -= 1
        else:
            raise IndexError("stack is empty")
    def peek(self):
        return self.start.item
    def size(self):
        return self.item
    
    
    
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
#s1.pop()
k = s1.size()
print(k)
        
    