class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def search(self, data):
        if self.start is not None:
            if self.start.next == self.start:
                if self.start.item == data:
                    return self.start
            else:
                temp = self.start
                while temp.next != self.start:
                    if temp.item == data:
                        return temp
                    temp = temp.next
                return temp

    def insear_At_first(self, data):
        n= Node(None, data)
        if self.start == None:
            n.prev = n
            n.next = n
            self.start = n
            
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n	
            self.start = n
            
    def insear_At_last(self, data):
        n= Node(None, data)
        if self.start == None:
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
    
    def inseart_after(self, value, data):
        val = self.search(value)
        if val is not None:
            n = Node(None, data)
            if self.start.next == self.start:
                if self.start == val:
                    n.prev = self.start
                    n.next = self.start
                    self.start.next = n
                    self.start.prev = n
            elif self.start.prev == val:
                n.prev = self.start.prev
                n.next = self.start
                self.start.prev.next = n
                self.start.prev = n
                
            else:
                n.prev = val
                n.next = val.next
                val.next.prev = n
                val.next = n
                
    def print(self):
        if self.start is not None:
            if self.start.next == self.start:
                print(self.start.item, end=' ')
            else:
                temp = self.start
                while temp.next != self.start:
                    print(temp.item, end=' ')
                    temp = temp.next
                print(temp.item)
                
    def delate_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
                
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
                
                
    def delate_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start.prev.next
                self.start.prev = self.start.prev.prev
                
                
    def delet_item(self, data):
        if self.start is not None:
            if self.start.next == self.start:
                if self.start.item == data:
                    self.start = None
                    
            elif self.start.item == data:
                return self.delate_first()
            
            elif self.start.prev.item == data:
                return self.delate_last()
            else:
                temp = self.start
                while temp.next != self.start:
                    if temp.item == data:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        break
                    temp = temp.next
    def __iter__(self):
        return CDLLIterator(self.start)
    
    
                    
                    
                    
class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.count = 0
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is not None:
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count == 1
        data = self.current.item
        self.current = self.current.next
        return data
            
    

                    
                
            
    
                
                
mylist = CDLL()
mylist.insear_At_first(13)
mylist.insear_At_first(10)
mylist.insear_At_last(20)
mylist.insear_At_last(30)
mylist.insear_At_last(40)
mylist.insear_At_last(50)
mylist.insear_At_last(60)
mylist.inseart_after(10, 12)
mylist.inseart_after(40, 45)
#mylist.delate_last()
#mylist.delate_first()
mylist.delet_item(30)
#print(mylist.is_empty())
mylist.print()
for x in mylist:
    print(x, end=' ')
    
print()
        
        
        


