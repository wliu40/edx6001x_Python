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
    
    def DFS(self, _root, target):        
        print self.stack
        if _root == None:
            return
        self.stack.append(_root.val)
        if _root.val == target:
            return
        
        self.DFS(_root.left, target)
        self.DFS(_root.right, target)
        if _root.val != target:
            self.stack.pop(-1)
        
        
            
l = [2,5,1,4,6]
bt = BSTree()
bt.convert(l)
bt.preorderTrav()
print ''
stack = []
bt.DFS(bt.getRoot(),1)
print bt.stack


            
