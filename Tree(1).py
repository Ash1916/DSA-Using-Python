class Node:
    def __init__(self, left = None, item = None, right = None):
        self.left = left
        self.item = item
        self.right = right
        
class Tree:
    def __init__(self):
        self.root = None
    
    def inseart(self, data):
        self.root = self.rinseart(self.root, data)
        
        
    def rinseart(self, root, data):
        if root is None:
            return Node(None, data)
        if data > root.item:
            root.right = self.rinseart(root.right, data)
        elif data < root.item:
            root.left = self.rinseart(root.left, data)
        return root
    def search(self, data):
        return self.research(self.root , data)
    def research(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            root = self.research(root.left , data)
        elif data > root.item:
            root = self.research(root.right, data)
        return root

    
    def Inorder(self):
        r = []
        self.rInorder(self.root, r)
        return r
    def rInorder(self,root, r):
        if root:
            self.rInorder(root.left, r)
            r.append(root.item)
            self.rInorder(root.right, r)
            
    def preorder(self):
        r = []
        self.rpreorder(self.root, r)
        return r
    def rpreorder(self,root, r):
        if root:
            r.append(root.item)
            self.rpreorder(root.left, r)
            self.rpreorder(root.right, r)
            
    def Postorder(self):
        r = []
        self.rPostorder(self.root, r)
        return r
    def rPostorder(self,root, r):
        if root:
            r.append(root.item)
            self.rPostorder(root.left, r)
            self.rPostorder(root.right, r)
            
    def Minvalue(self, data):
        temp = data
        while  temp.left is not None:
            temp = temp.left
        return temp.item
        
    def Maxvalue(self, data):
        temp = data
        while  temp.right is not None:
            temp = temp.right
        return temp.item
    
    def Delete(self, data):
        self.root = self.rDelete(self.root, data)
    def rDelete(self, root, data):
        #val = self.search(data)
        if root is None:
            return root
        if data < root.item:
            root.left = self.rDelete(root.left, data)
        elif data > root.item:
            root.right = self.rDelete(root.right, data)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                root.item = self.Minvalue(root)
                self.Delete(root.item)
        return root
                
                
            
            
    
    def size(self):
        pass
            
            
            

T1 = Tree()
T1.inseart(10)
T1.inseart(100)
T1.inseart(95)
T1.inseart(30)
T1.inseart(40)
T1.inseart(60)
T1.inseart(70)
T1.inseart(90)
#k = T1.preorder()
#l=T1.search(90)
T1.Delete(90)
M = T1.Inorder()
print(M)

        
            
            
         