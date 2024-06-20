class Node:
    def __init__(self, prev = None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class Deque:
    def __init__(self,fornt= None, rear=None):
        self.front = fornt
        self.rear = rear
        self.item_count = 0
        
    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        n = Node(None,data)
        if self.is_empty():
            self.front = n      
        else:
            n.prev = self.rear
            self.rear.next = n
        self.rear = n
        self.item_count += 1
        
    def insert_rear(self,data):
        n = Node(None,data)
        if self.is_empty():
            self.front = n
        else:
            n.next = self.front
            self.front.prev = n
        self.front = n
        self.item_count += 1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deuqe is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
            self.item_count -= 1
        else:
            self.rear.prev.next = None
            self.rear = self.rear.prev
            self.item_count -= 1
            
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deuqe is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
            self.item_count -= 1
        else:
            self.front.next.prev = None
            self.front =self.front.next
            self.item_count -= 1
            
    def get_front(self):
        return self.rear.item
    def get_rear(self):
        return self.front.item
    def size(self):
        return self.item_count
    
    
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
