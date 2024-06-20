class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None

    def search(self, data):
        if self.last is None:
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
            
    def inseart_at_start(self, data):
        if self.last is None:
            n = Node(data)
            self.last = n
            n.next = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n

    def inseart_at_last(self, data):
        if self.last is None:
            n = Node(data, n)
            self.last = n
            
        else:
            n = Node(data, self.last.next)
            self.last.next = n
            self.last = n

    def inseart_after(self, value, data):
        val = self.search(value)
        if val is not None:
            if val == self.last:
                n = Node(data,self.last.next)
                self.last.next = n
                self.last = n
            else:
                n = Node(data,val.next)
                val.next = n
                
            '''
            temp = self.last.next
            while temp != self.last:
                if temp.item == val:
                    if temp.next == self.last:
                        n = Node(data,temp.next)
                        temp.next = n
                        self.last = n
                    else:
                        n = Node(data,temp.next)
                        temp.next = n
                temp = temp.next
            if temp.item == data:
                n = Node(data,temp.next)
                temp.next = n
            '''

    def print(self):
        if self.last == None:
            return None
        else:
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)
            
        
    def delet_first_item(self):
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
            
    def delet_last_item(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
            
    def delet_item(self, data):
        val = self.search(data)
        if val is not None:
            if self.last.next == self.last:
                if self.last == data:
                    self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                if temp.next == data:
                    temp.next = self.last.next
                    self.last = temp

class Stack:
    def __init__(self):
        
        self.top = CLL()
        self.item_count = 0
        
    def push(self,data):
        self.top.inseart_at_start(data)
        self.item_count += 1
        
    def pop(self):
        K = self.top.delet_first_item
        self.item_count -= 1
        return K
        
    def peek(self):
        self.top()
        val = self.start(self.start)
        
        print(val)
    def size(self):
        return self.item_count
        
        
'''        
        
        
                    
mylist = CLL()
mylist.inseart_at_start(13)
mylist.inseart_at_start(10)
#print(mylist.is_empty())
mylist.inseart_at_last(20)
mylist.inseart_at_last(30)
mylist.inseart_at_last(40)
mylist.inseart_after(10, 12)
mylist.inseart_after(40, 45)
#mylist.delet_last_item()
#mylist.delet_first_item()
#mylist.delet_item(30)
mylist.print()
'''
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.pop()
k=s1.peek()
print(k)
    