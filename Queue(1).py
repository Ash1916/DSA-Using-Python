class Queue:
    def __init__(self):
        self.item = []
        
    def is_empty(self):
        return len(self.item)== 0
    
    def enqueue(self,data):
        self.item.append(data)
        
    def dequeue(self):
        if self.item is not None:
            self.item.pop(0)
        else:
            raise IndexError("stack is empty")
        
    def get_front(Self):
        print(Self.item[0])
    def get_rear(self):
        print(self.item[-1])
    def size(self):
        print(len(self.item))
    
s1=Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
s1.enqueue(40)
s1.enqueue(50)
s1.enqueue(60)
s1.get_front()
s1.get_rear()
s1.dequeue()
s1.get_front()
s1.get_rear()

