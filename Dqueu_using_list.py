class Deque:
    def __init__(self):
        self.start = []
        
    def is_empty(self):
        return len(self.start) == 0
        
    def insert_front(self, data):
        self.start.append(data)
    def insert_rear(self,data):
        self.start.insert(0,data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.start.pop()
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.start.pop(0)
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.start[-1]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.start[0]
    def size(self):
        return len(self.start)
    
D1=Deque()
D1.insert_front(20)
D1.insert_front(10)
D1.insert_rear(30)
D1.insert_rear(40)
print(D1.get_front(), D1.get_rear())
print(D1.size())
D1.delete_front()
D1.delete_rear()
print(D1.get_front(), D1.get_rear())
print(D1.size())


