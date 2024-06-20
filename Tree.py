from typing import Any


class Node:
    def __init__(self, left = None, item = None, right = None):
        self.left = left
        self.item = item
        self.right = right
        
class Tree:
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return self.root == None
    
    def push(self, data):
        n = Node(None, data)
        if self.root is None:
            self.root = n
        else:
            temp = self.root
            while temp.item != n.item:
                if temp.left < n.item:
                    temp = temp.right
                elif temp.right > n.item:
                    temp = temp.left
                elif temp.left < n.item < temp.right:
                    if temp.item < n.item:
                        n.right = temp.right
                        temp.right = n
                    elif temp.item > n.item:
                        n.left = temp.left
                        temp.left = n
                return n
        
    def search(self, data):
        temp = self.root
        while temp.item != data:
            pass
            
    
    def Inorder(self):
        temp = self.root
        pass
    def preorder(self):
        pass
    def postorder(self):
        pass
    
T1 = Tree()
T1.push(10)
T1.push(100)
T1.push(95)
T1.push(30)
T1.push(40)
T1.push(60)
T1.push(70)
T1.push(90)
k = T1
print(k)
        
            
            
         