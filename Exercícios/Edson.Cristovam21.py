class NodeTree:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
        self._papa = None

    def __str__(self):
        return str(self.getData())
    def getData(self):
        return self._data
    def getLeft(self):
        return self._left
    def getRight(self):
        return self._right
    def getFather(self):
        return self._papa

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
            self._text = self._text+', '+str(root.getData())
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
        
        if(root.getLeft() == None):
            #print(root,"mini)
            return root
        self.mini(root.getLeft())
        '''
        while 1:
            if(root.getLeft() != None):
                root = root.getLeft()
            else:
                return root'''

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
        if(root.getData() == root.getLeft().getData()):
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
                return 0
        if(root.getLeft() != None):
            x = self.maxi(root.getLeft())
            if(x.getData() == root.getData()):
                return self.predecessor(x)
            else:
                return x
                
        else:    
            dad = root.getFather()
            while(dad != None):
                if(root == dad.getRight()):
                    break
                root = dad
                dad = dad.getFather()
            if(dad == None):
                return 0
            return dad

    def search(self, data, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        if(root == None or data == root.getData()):
            return root
        elif(data > root.getData()):
            return self.search(data, root.getRight())
        else:
            return self.search(data, root.getLeft())

    def insert(self, data):
        node = NodeTree(data)
        if(self.getRoot() == None):
            self.setRoot(node)
        else:
            x = self.getRoot()
            while x != None:
                if(data > x.getData()):
                    y,x = x, x.getRight()
                else:
                    y,x = x, x.getLeft()
            if(data > y.getData()):
                y.setRight(node)
            else:
                y.setLeft(node)
            node.setFather(y)

    def crescent(self, root="DEFAULT"):
        global lista
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                lista.append(0) #print('Árvore vazia.')
        
        if(root != None):
            self.crescent(root.getLeft())
            lista.append(root.getData()) #print(root, end=' ')
            self.crescent(root.getRight())
        
    def decrescent(self, root="DEFAULT"):
        global lista
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                lista.append(0) #print('Árvore vazia.')

        if(root != None):
            self.decrescent(root.getRight())
            lista.append(root.getData()) #print(root, end=' ')
            self.decrescent(root.getLeft())

    def preOrder(self, root="DEFAULT"):
        global lista
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                lista.append(0) #print('Árvore vazia.')

        if(root != None):
            lista.append(root.getData()) #print(root, end=' ')
            self.preOrder(root.getLeft())
            self.preOrder(root.getRight())

    def posOrder(self, root="DEFAULT"):
        global lista
        if(root == "DEFAULT"):
            root = self.getRoot()
            if(root == None):
                lista.append(0) #print('Árvore vazia.')

        if(root != None):
            self.posOrder(root.getLeft())
            self.posOrder(root.getRight())
            lista.append(root.getData()) #print(root, end=' ')
            
    def delete(self, data, root="DEFAULT"):
        if(root == "DEFAULT"):
            root = self.getRoot()
        z = self.search(data)
        if(z == None):
            #print('Elemento não pertence a árvore.')
            return z
        if(z.getLeft() == None or z.getRight() == None):
            y = z
        else:
            y = self.maxi(z.getLeft())#self.successor(z)
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
            z.setData(y.getData())
        return y


if(__name__ == '__main__'):
    entrada = input().split()
    arvore = BinaryTree()
    lista = []
    resposta = []
    
    for x in range(len(entrada)):
        #print('lp atual',entrada[x], arvore)
        if(entrada[x] == 'A'):
            arvore.insert(int(entrada[x+1]))

        elif(entrada[x] == 'B'):
            arvore.delete(int(entrada[x+1]))

        elif(entrada[x] == 'C'):
            if(arvore.search(int(entrada[x+1])) != None):
                predecessor = arvore.predecessor(arvore.search(int(entrada[x+1])))
                if(predecessor != 0):
                    resposta.append(str(predecessor.getData())+';')
                else:
                   resposta.append('0;')
            else:
               resposta.append('0;')
        
        elif(entrada[x] == 'PRE'):
            arvore.preOrder()
            resposta.append(' '.join([str(x) for x in lista])+';')
            lista = []

        elif(entrada[x] == 'IN'):
            arvore.crescent()
            resposta.append(' '.join([str(x) for x in lista])+';')
            lista = []

        elif(entrada[x] == 'POST'):
            arvore.posOrder()
            resposta.append(' '.join([str(x) for x in lista])+';')
            lista = []

    print(' '.join(resposta))
