from Binary_Tree_NEW import *

class NodeAVL(NodeTree):
    def __init__(self, key, data=None):
        self._key = key
        self._data = data
        self._left = None
        self._right = None
        self._papa = None
        self._h = 0

    def getHeight(self):
        return self._h
    def setHeight(self, Height):
        self._h = Height
    
class AVLTree(BinaryTree):
    def rotationLL(self, root):
        left = root.getLeft()

        left.setFather(root.getFather())
        if(root.getFather() == None):
            self.setRoot(left)
        elif(root.getFather().getLeft() == root):
            root.getFather().setLeft(left)
        else:
            root.getFather().setRight(left)

        root.setLeft(left.getRight())
        if(root.getLeft() != None):
            root.getLeft().setFather(root)

        left.setRight(root)
        root.setFather(left)

    def rotationRR(self, root):
        right = root.getRight()

        right.setFather(root.getFather())
        if(root.getFather() == None):
            self.setRoot(right)
        elif(root.getFather().getLeft() == root):
            root.getFather().setLeft(right)
        else:
            root.getFather().setRight(right)

        root.setRight(right.getLeft())
        if(root.getRight() != None):
            root.getRight().setFather(root)

        right.setLeft(root)
        root.setFather(right)

    def rotationLR(self, root):
        self.rotationRR(root.getLeft())
        self.rotationLL(root)

    def rotationRL(self, root):
        self.rotationLL(root.getRight())
        self.rotationRR(root)

    def insert(self, key, data=None):
        node = NodeAVL(key, data)
        if(self.getRoot() == None):
            self.setRoot(node)
        else:
            x = self.getRoot()
            while x != None:
                if(key > x.getKey()):
                    y,x = x, x.getRight()
                elif(key < x.getKey()):
                    y,x = x, x.getLeft()
                else:
                    print("Chave já pertence a árvore.")
                    return 0
            if(key > y.getKey()):
                y.setRight(node)
            else:
                y.setLeft(node)
            node.setFather(y)
        #self.heightCalc()
        self.balance2(node) #self.balance(node)

    def delete(self, key, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        z = self.search(key)
        if(z == None):
            print('Elemento não pertence a árvore.')
            return z
        if(z.getLeft() == None or z.getRight() == None):
            y = z
        else:
            y = self.successor(z)
        if(y.getLeft() != None):
            x = y.getLeft()
        else:
            x = y.getRight()
        if(x != None):
            x.setFather(y.getFather())
        if(y.getFather() == None):
            self.setRoot(x)
        else:
            if(y == y.getFather().getLeft()):
                y.getFather().setLeft(x)
            else:
                y.getFather().setRight(x)
        if(y != z):
            z.setKey(y.getKey())
            z.setData(y.getData())

        self.heightCalc()
        self.balance(y)
        return y
    
    def balance(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        if(root == None):
            return
            
        fb = self.fBalance(root)
        if(fb >= 2):
            if(self.fBalance(root.getRight()) < 0):
                self.rotationRL(root)
            else:
                self.rotationRR(root)
            self.heightCalc()
            if(root.getFather() != None):
                self.balance(root)
        elif(fb <= -2):
            if(self.fBalance(root.getLeft()) > 0):
                self.rotationLR(root)
            else:
                self.rotationLL(root)
            self.heightCalc()
            if(root.getFather() != None):
                self.balance(root)
        else:
            if(root.getFather() != None):
                self.balance(root.getFather())

    def balance2(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        if(root == None):
            return
            
        fb = self.fBalance2(root) #self.fBalance(root)
        if(fb >= 2):
            if(self.fBalance(root.getRight()) < 0):
                self.rotationRL(root)
            else:
                self.rotationRR(root)
            self.heightCalc()
            if(root.getFather() != None):
                self.balance(root)
        elif(fb <= -2):
            if(self.fBalance(root.getLeft()) > 0):
                self.rotationLR(root)
            else:
                self.rotationLL(root)
            self.heightCalc()
            if(root.getFather() != None):
                self.balance(root)
        else:
            if(root.getFather() != None):
                self.balance2(root.getFather()) #self.balance(root.getFather())

    '''def fBalance(self, root):
        if(root.getLeft() == None):
            left = -1
        else:
            left = root.getLeft().getHeight()
        
        if(root.getRight() == None):
            right = -1
        else:
            right = root.getRight().getHeight()

        return (right - left)'''
        
    def heightCalc(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        if(root == None):
            return -1
        else:
            #print(root)
            left = self.heightCalc(root.getLeft())
            right = self.heightCalc(root.getRight())
            root.setHeight(1+self.maximium(left, right))
            return root.getHeight()

    def fBalance(self, root):
        if(root.getLeft() == None):
            left = -1
        else:
            left = root.getLeft().getHeight()
        
        if(root.getRight() == None):
            right = -1
        else:
            right = root.getRight().getHeight()

        #root.setHeight(1+self.maximium(left,right))        
        return (right - left)
        
    def fBalance2(self, root):
        if(root.getLeft() == None):
            left = -1
        else:
            left = root.getLeft().getHeight()
        
        if(root.getRight() == None):
            right = -1
        else:
            right = root.getRight().getHeight()

        root.setHeight(1+self.maximium(left,right))        
        return (right - left)

    def maximium(self, A, B):
        #print(A,B)
        if(A >= B):
            return A
        else:
            return B

if(__name__ == "__main__"):
    '''
    x = AVLTree()
    x.insert(1)
    x.insert(3)
    x.insert(2)
    print(x.getRoot())
    #x.rotationRL(x.getRoot())
    print(x.getRoot())
    print(x.getRoot().getLeft())
    print(x.getRoot().getRight())
    print(x)
    '''
    
    from time import sleep, time

    from random import randint
    x = AVLTree()
    start = time()

    for y in range(0,10000,100):
        start2 = time()
        for i in range(100):
            z = y+(i+1)#randint(0,10000000)
            #print(z, end=' ')
            x.insert(z)

        end2 = time()
        print('Inserindos:', z, 'TEMPO:',end2-start2)
            

    end = time()
    print()
    print('AVL 3\nAltura da RAIZ.',x.getRoot().getHeight(), 'FB:', x.fBalance(x.getRoot()))
    print('Número de Elementos', len(x))
    print('TEMPO:',end-start)

    '''sleep(10)
    start = time()
    for y in range(20240):
        z = randint(0,10000)
        x.delete(z)

    end = time()
    print()
    print('Altura da RAIZ.',x.getRoot().getHeight(), 'FB:', x.fBalance(x.getRoot()))
    print('Número de Elementos', len(x))
    print('TEMPO:',end-start)'''
