class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
    
class BSTree():
    def __init__(self):
        self.root = None
        self.stack = []
        self.flag = False
        
    def preorderTrav(self):
        self.preorderTravHelper(self.root)
        
    def preorderTravHelper(self, startNode):
        if startNode != None:
            print startNode, " ",
            self.preorderTravHelper(startNode.left)
            self.preorderTravHelper(startNode.right)
            
    def insert_Iterative(self, val):
        newNode = Node(val)
        if self.root == None:            
            self.root = newNode
            return
        curNode = self.root
        while True:
            if val < curNode.val:
                if curNode.left != None:
                    curNode = curNode.left
                else:
                    curNode.left = newNode                    
                    break
            else:
                if curNode.right != None:
                    curNode = curNode.right
                else:
                    curNode.right = newNode
                    break
    def convert(self, l):
        for i in l:
            self.insert_Iterative(i)
            
    def getRoot(self):
        return self.root
    
    flag = False
    def DFS(self, _root, target):        
        
        if _root == None or self.flag == True:
            return
        self.stack.append(_root.val)
        if _root.val == target:
            self.flag = True
            return
        
        self.DFS(_root.left, target)
        self.DFS(_root.right, target)
        if self.stack[-1] != target:
            self.stack.pop(-1)
        
        
            
l = [2,5,1,4]
bt = BSTree()
bt.convert(l)
#bt.preorderTrav()
print ''
#stack = []
#flag = False
bt.DFS(bt.getRoot(),6)
print bt.stack
print bt.flag

            
