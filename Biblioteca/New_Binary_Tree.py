class NodeTree:
    def __init__(self, key, data=None):
        self.__key = key
        self.__data = data
        self.__father = None
        self.__left = None
        self.__right = None

    def getKey(self):
        return self.__key
    def getData(self):
        return self.__data
    def getFather(self):
        return self.__father
    def getLeft(self):
        return self.__left
    def getRight(self):
        return self.__right

    def setKey(self, key):
        self.__key = key
    def setData(self, data):
        self.__data = data
    def setFather(self, node):
        self.__father = node
    def setLeft(self, node):
        self.__left = node
    def setRight(self, node):
        self.__right = node

    def __str__(self):
        return str(self.getData())

    def __le__(self, another): #__le__ refere-se a comparação menor ou igual, aparentemente com está função o Python já a utiliza para definir o __ge__ que seria o maior ou igual
        return self.getKey() <= another.getKey()

    def __lt__(self, another): #__lt__ refere-se a comparação menor, aparentemente com está função o Python já a utiliza para definir o __gt__ que seria o maior.
        return self.getKey() < another.getKey()

    def __eq__(self, another): #__eq__ refere-se a comparação igual, aparentemente com está função o Python já a utiliza para definir o __ne__ que seria o diferente.
        if(type(another) == NodeTree):
            return self.getKey() == another.getKey()
        else:
           return False 
    
class BinaryTree:
    def __init__(self):
        self.__root = None
        self.__length = 0
        self.__txt = ''

    def __len__(self):
        return self.__length

    def __str__(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            self.__txt = ''
            root = self.__root
            if(root == None):
                return 'Árvore Vazia.'
        if(root != None):            
            self.__str__(root.getLeft())
            self.__txt += str(root.getKey())+', '
            self.__str__(root.getRight())

        return '['+self.__txt[:-2]+']'

    
    def insert(self, key, data=None):
        node = NodeTree(key, data)

        if(self.__root == None):
            self.__root = node
            self.__length += 1
        else:
            x = self.__root
            y = None

            while x != None:
                if(key < x.getKey()):
                    x, y = x.getLeft(), x
                elif(key > x.getKey()):
                    x, y = x.getRight(), x
                else:
                    return print('Chave já existe na árvore')#0

            node.setFather(y)
            self.__length += 1
            if(key < y.getKey()):
                y.setLeft(node)
            else:
                y.setRight(node)
            '''
            if(node.getFather().getLeft() == node):
                print(node, 'é filho esquerdo de', node.getFather())
                print(' '*(len(str(node.getKey()))-1), node.getFather())
                print(' '*(len(str(node.getKey()))-2),' /')
                print(' '*(len(str(node.getKey()))-2),'/')
                print(node)
                
            else:
                print(node, 'é filho direito de', node.getFather())
                print(node.getFather())
                print(' '*(len(str(node.getKey()))-2),'\\')
                print(' '*(len(str(node.getKey()))-2),' \\')
                print(' '*(len(str(node.getKey()))-1), node)
            '''
                              

    def search(self, key):
        root = self.__root

        while root != None and key != root.getKey():
            if(key < root.getKey()):
                root = root.getLeft()
            else:
                root = root.getRight()
                
        return root

    def delete(self, key):
        z = self.search(key)
        if(z == None):
            print('Elemento não pertence a árvore.')
            return z

        if z.getLeft() == None or z.getRight() == None:
            y = z
        else:
            print('2 f')
            y = self.successor(z)

        if(y.getLeft() != None):
            x = y.getLeft()
        else:
            x = y.getRight()

        if(x != None):
            x.setFather(y.getFather())

        if(y.getFather() == None):
            self.__root = x
        else:
            if(y == y.getFather().getLeft()):
                y.getFather().setLeft(x)
            else:
                y.getFather().setRight(x)

        if(y != z):
            z.setKey(y.getKey())
            z.setData(y.getData())

        self.__length -= 1    
        return y

    
    def mini(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == None):
                return 'Árvore Vazia.'

        while 1:
            if(root.getLeft() != None):
                root = root.getLeft()
            else:
                return root
                
        '''
        if(root.getLeft() != None):
            self.mini(root.getLeft())
        else:
            print(root.getKey())
            return root.getKey()
        '''

    def maxi(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == None):
                return 'Árvore Vazia.'

        while 1:
            if(root.getRight() != None):
                root = root.getRight()
            else:
                return root

    def successor(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == None):
                return 'Árvore Vazia.'

        if(root.getRight() != None):
            return self.mini(root.getRight())

        dad = root.getFather()
        while(dad != None):
            if(root == dad.getLeft()):
                break
            root = dad
            dad = dad.getFather()
             
        return dad

    def predecessor(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == None):
                return 'Árvore Vazia.'

        if(root.getLeft() != None):
            return self.maxi(root.getRight())

        dad = root.getFather()
        while(dad != None):
            if(root == dad.getRight()):
                break
            root = dad
            dad = dad.getFather()
             
        return dad


if(__name__ == '__main__'):
    tree = BinaryTree()

    from random import randint

    for x in range(10):
        y = randint(0,1000)
        print(y)#print(y,end=' ')
        tree.insert(y, str(y))
        print(tree)

    #print()
    #print(tree)
    #print(tree.mini())
    #print(tree.maxi())
