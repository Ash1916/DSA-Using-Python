class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0
        
    def is_empty(self):
        return self.start == None
    
    def push(self,data):
        n = Node(data,self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if self.start is not None:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if self.start is None:
            raise IndexError("stack is empty")
        else:
            return self.start.item
    def size(self):
        return self.item_count
            
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
k=s1.pop()
l = s1.peek()
print(k,l)