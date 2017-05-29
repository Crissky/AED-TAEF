class NodeTree:
    def __init__(self, key, data=None):
        self._key = key
        self._data = data
        self._left = None
        self._right = None
        self._papa = None

    def __str__(self):
        return str(self.getKey())
    def getKey(self):
        return self._key
    def getData(self):
        return self._data
    def getLeft(self):
        return self._left
    def getRight(self):
        return self._right
    def getFather(self):
        return self._papa

    def setKey(self, key):
        self._key = key
    def setData(self, data):
        self._data = data
    def setLeft(self, left):
        self._left = left
    def setRight(self, right):
        self._right = right
    def setFather(self, father):
        self._papa = father
    
class BinaryTree:
    def __init__(self):
        self._root = None        
        
    def __str__(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            self._text = ''
            if(root == None):
                return 'Árvore vazia.'
        if(root != None):
            self.__str__(root.getLeft())
            self._text = self._text+', '+str(root.getKey())
            self.__str__(root.getRight())
        return '['+self._text[2:]+']'

    def __len__(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            self._count = 0
            if(root == None):
                return 0
        if(root != None):
            self.__len__(root.getLeft())
            self._count += 1
            self.__len__(root.getRight())
        return self._count

    def getRoot(self):
        return self._root
    def setRoot(self, root):
        self._root = root    
    
    def mini(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                return root
        '''
        print(root,"mini")
        if(root.getLeft() == None):
            return root
        self.mini(root.getLeft())
        '''
        while 1:
            if(root.getLeft() != None):
                root = root.getLeft()
            else:
                return root

    def maxi(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                return root
        '''
        print(root,"maxi")
        if(root.getRight() == None):
            return root

        self.maxi(root.getRight())
        '''
        while 1:
            if(root.getRight() != None):
                root = root.getRight()
            else:
                return root

    '''def leftNoEqual(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                return root
        if(root.getLeft() == None):
            return None
        if(root.getKey() == root.getLeft().getKey()):
            return self.leftNoEqual(root.getLeft())
        else:
            return root.getLeft()'''
    
    def successor(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                return root
        if(root.getRight() != None):
            return self.mini(root.getRight())
        dad = root.getFather()
        while(dad != None):
            if(root == dad.getLeft()):
                break
            root = dad
            dad = dad.getFather()
            
        return dad

    def predecessor(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                return root
        if(root.getLeft() != None):
            x = self.maxi(root.getLeft())
            while 1:
                if(x.getKey() == root.getKey()):
                    if(x.getLeft() != None):
                        x = self.maxi(x.getLeft())
                    else:
                        break
                else:
                    return x
            while 1:
                if(x.getFather().getKey() == root.getKey()):
                    x = x.getFather()
                else:
                    return x.getFather()
        dad = root.getFather()
        while(dad != None):
            if(root == dad.getRight()):
                break
            root = dad
            dad = dad.getFather()
        return dad

    def search(self, key, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        if(root == None or key == root.getKey()):
            return root
        elif(key > root.getKey()):
            return self.search(key, root.getRight())
        else:
            return self.search(key, root.getLeft())

    def search20(self, key, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            self.__searchCount = 0

        self.__searchCount += 1
        if(root == None or key == root.getKey()):
            return self.search20loop(root)
            
        elif(key > root.getKey()):
            return self.search20(key, root.getRight())
        else:
            return self.search20(key, root.getLeft())

    def search20loop(self, root):
        for x in range(self.__searchCount, 20):
            self.__searchCount += 1
            if(root == root):
                if(root == root):
                    continue
        return root
        
    def insert(self, key, data=None):
        node = NodeTree(key, data)
        if(self.getRoot() == None):
            self.setRoot(node)
        else:
            x = self.getRoot()
            while x != None:
                if(key > x.getKey()):
                    y,x = x, x.getRight()
                else:
                    y,x = x, x.getLeft()
            if(key > y.getKey()):
                y.setRight(node)
            else:
                y.setLeft(node)
            node.setFather(y)

    def crescent(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                print('Árvore vazia.')
        if(root != None):
            self.crescent(root.getLeft())
            print(root, end=' ')
            self.crescent(root.getRight())

    def decrescent(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                print('Árvore vazia.')
        if(root != None):
            self.decrescent(root.getRight())
            print(root, end=' ')
            self.decrescent(root.getLeft())

    def preOrder(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                print('Árvore vazia.')
        if(root != None):
            print(root, end=' ')
            self.preOrder(root.getLeft())
            self.preOrder(root.getRight())

    def posOrder(self, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                print('Árvore vazia.')
        if(root != None):
            self.posOrder(root.getLeft())
            self.posOrder(root.getRight())
            print(root, end=' ')
            
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
        return y
'''
from random import randint
arv = BinaryTree()
#arv.insert(1000)
for x in range(10):
    y = randint(100,1000)
    arv.insert(y)
    print(y, end=' ')
print('')
print(arv.mini())
print(arv.maxi())
'''
'''x = BinaryTree()
x.insert(5)
x.insert(1)
x.insert(2)
x.insert(7)
x.insert(6)
x.insert(7)
print(x.predecessor(x.search(7)))'''
'''x.delete(2)
x.delete(6)
x.preOrder()
print()
x.crescent()
print()
x.posOrder()
print()'''
'''
x = BinaryTree()
x.insert(8)
x.insert(3)
x.insert(1)
x.insert(6)
x.insert(4)
x.insert(7)
x.insert(10)
x.insert(14)
x.insert(13)

x.preOrder()
print()
x.crescent()
print()
x.posOrder()
print()
'''
