class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def Is_empy(self):
         return self.start == None

    def Inseart_at_start(self,data):
        n = Node(None,data,self.start)
        self.start = n
        self.start.prev = n

    def Inseart_at_last(self, data):
        temp = self.start
        if temp is None:
            n = Node(None,data)
        else:
            while temp.next is not None:
                temp = temp.next
            n = Node(temp.prev,data)
            temp.next = n

    def Search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

    def Inseat_after(self, value, data):
        val = self.Search(value)
        if val is not None:    
            n = Node(val, data, val.next)
            val.next.prev = n
            val.next  = n


    def Print(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next

    def Delet_first(self):
        if self.start is not None:
            self.start = self.start.next
            self.start.next.prev = None

    def Delet_last(self):
        if self.start is not None:
            if self.start.next == None:
                self.start = None
            else:
                temp=self.start
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None

    def Detel_item(self, value):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == value:
                    if temp.next == None:
                        temp.prev.next = None
                    elif temp.prev == None:
                        self.start = temp.next
                    else:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                    break
                temp=temp.next
                

    
              

        




mylist = DLL()
mylist.Inseart_at_start(10)
mylist.Inseart_at_last(20)
mylist.Inseart_at_last(30)
mylist.Inseart_at_last(40)
mylist.Inseat_after(10, 15)
mylist.Detel_item(40)
mylist.Print()
