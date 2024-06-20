
class Stack(list):
    def is_emplty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)
        
    def pop(self):
        if self is not None:
            return super().pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if self is not None:
            return self[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        if self is not None:
            return len(self)
        else:
            raise IndexError("Stack is empty")
        
    def insert(self, index, data):
        raise AttributeError("this attribute is not exist")

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.pop()
k=s1.peek()
print(k)
    