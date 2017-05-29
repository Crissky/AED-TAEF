from New_Binary_Tree import *

class NodeTreeRB(NodeTree):
    def __init__(self, key, data=None):
        self.__color = 'red'
        super().__init__(key, data)
    
    def getColor(self):
        return self.__color
    def setColor(self, color):
        if(color.lower() == 'red'):
            self.__color = 'red'
        elif(color.lower() == 'black'):
            self.__color = 'black'
    def changeColor(self):
        if(self.getColor() == 'red'):
            self.__color = 'black'
        else:
            self.__color = 'red'

    def __str__(self):
        return str(self.getKey())#+' '+self.getColor()

    def __eq__(self, another):
        if(type(another) == NodeTreeRB):
            return self.getKey() == another.getKey()
        else:
           return False 

class RBTree:
    def __init__(self):
        self.__ward = NodeTreeRB(None)
        self.__root = self.__ward
        self.__length = 0
        self.__txt = ''

        self.wardFixUP()

    def wardFixUP(self):
        self.__ward.setColor('black')
        self.__ward.setFather(self.__ward)
        self.__ward.setLeft(self.__ward)
        self.__ward.setRight(self.__ward)

    #Retorna uma lista de chaves
    def list(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            self.__txt = []
            root = self.__root
            if(root == self.__ward):
                return []
        if(root != self.__ward):            
            self.list(root.getLeft())
            self.__txt.append(root.getKey())
            self.list(root.getRight())

        return self.__txt

    #Retorna uma lista de Objetos
    def list2(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            self.__txt = []
            root = self.__root
            if(root == self.__ward):
                return []
        if(root != self.__ward):            
            self.list2(root.getLeft())
            self.__txt.append(root)
            self.list2(root.getRight())

        return self.__txt

    def __str__(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            self.__txt = ''
            root = self.__root
            if(root == self.__ward):
                return 'Árvore Vazia.'
        if(root != self.__ward):            
            self.__str__(root.getLeft())
            self.__txt += str(root.getKey())+', '
            self.__str__(root.getRight())

        return self.__txt[:-2]
        
    def __len__(self):
        return self.__length
    
    def rotationLL(self, root): #Rotação a Direita
        left = root.getLeft()
 
        left.setFather(root.getFather())
        if(root.getFather() == self.__ward):
            self.__root = left
        elif(root.getFather().getLeft() == root):
            root.getFather().setLeft(left)
        else:
            root.getFather().setRight(left)
 
        root.setLeft(left.getRight())
        if(root.getLeft() != self.__ward):
            root.getLeft().setFather(root)
 
        left.setRight(root)
        root.setFather(left)
 
    def rotationRR(self, root): #Rotação a Esquerda
        right = root.getRight()
 
        right.setFather(root.getFather())
        if(root.getFather() == self.__ward):
            self.__root = right
        elif(root.getFather().getLeft() == root):
            root.getFather().setLeft(right)
        else:
            root.getFather().setRight(right)
 
        root.setRight(right.getLeft())
        if(root.getRight() != self.__ward):
            root.getRight().setFather(root)
 
        right.setLeft(root)
        root.setFather(right)
 
    def rotationLR(self, root): #Dupla Rotação a Direita
        self.rotationRR(root.getLeft())
        self.rotationLL(root)
 
    def rotationRL(self, root): #Dupla Rotação a Esquerda
        self.rotationLL(root.getRight())
        self.rotationRR(root)

    def changeColors(self, node):
        node.changeColor()
        if(node.getLeft() != self.__ward):
            node.getLeft().changeColor()
        if(node.getRight() != self.__ward):
            node.getRight().changeColor()

    def search(self, key):
        root = self.__root

        while root != self.__ward and key != root.getKey():
            if(key < root.getKey()):
                root = root.getLeft()
            else:
                root = root.getRight()
                
        return root

    def mini(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == self.__ward):
                return 'Árvore Vazia.'

        while 1:
            if(root.getLeft() != self.__ward):
                root = root.getLeft()
            else:
                return root

    def maxi(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == self.__ward):
                return 'Árvore Vazia.'

        while 1:
            if(root.getRight() != self.__ward):
                root = root.getRight()
            else:
                return root

    def successor(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == self.__ward):
                return 'Árvore Vazia.'

        if(root.getRight() != self.__ward):
            return self.mini(root.getRight())

        dad = root.getFather()
        while(dad != self.__ward):
            if(root == dad.getLeft()):
                break
            root = dad
            dad = dad.getFather()
             
        return dad

    def predecessor(self, root='DEFAULT'):
        if(root == 'DEFAULT'):
            root = self.__root
            if(root == self.__ward):
                return 'Árvore Vazia.'

        if(root.getLeft() != self.__ward):
            return self.maxi(root.getRight())

        dad = root.getFather()
        while(dad != self.__ward):
            if(root == dad.getRight()):
                break
            root = dad
            dad = dad.getFather()
             
        return dad
    
    def insert(self, key, data=None):
        node = NodeTreeRB(key, data)
        node.setFather(self.__ward)
        node.setLeft(self.__ward)
        node.setRight(self.__ward)

        if(self.__root == self.__ward):
            self.__root = node
        else:
            x = self.__root
            y = self.__ward

            while x != self.__ward:
                if(key < x.getKey()):
                    x, y = x.getLeft(), x
                elif(key > x.getKey()):
                    x, y = x.getRight(), x
                else:
                    return 0#print('Chave',key, 'já existe na árvore')#0

            node.setFather(y)
            if(key < y.getKey()):
                y.setLeft(node)
            else:
                y.setRight(node)

        self.__length += 1
        self.RBInsertFixUP(node)
        return 1
    
    def RBInsertFixUP(self, node):
        while node.getFather().getColor() == 'red':
            if(node.getFather() == node.getFather().getFather().getLeft()):
                y = node.getFather().getFather().getRight()

                if(y.getColor() == 'red'):
                    node.getFather().setColor('black')
                    y.setColor('black')
                    node.getFather().getFather().setColor('red')
                    node = node.getFather().getFather()
                else:
                    if(node == node.getFather().getRight()):
                        node = node.getFather()
                        self.rotationRR(node)

                    node.getFather().setColor('black')
                    node.getFather().getFather().setColor('red')
                    self.rotationLL(node.getFather().getFather())

            elif(node.getFather() == node.getFather().getFather().getRight()):
                y = node.getFather().getFather().getLeft()
            
                if(y.getColor() == 'red'):
                    node.getFather().setColor('black')
                    y.setColor('black')
                    node.getFather().getFather().setColor('red')
                    node = node.getFather().getFather()
                else:
                    if(node == node.getFather().getLeft()):
                        node = node.getFather()
                        self.rotationLL(node)

                    node.getFather().setColor('black')
                    node.getFather().getFather().setColor('red')
                    self.rotationRR(node.getFather().getFather())

        self.__root.setColor('black')

    def delete(self, key):
        z = self.search(key)
        if(z == self.__ward):
            #print(key, 'não pertence a árvore.')
            return 0#z

        if z.getLeft() == self.__ward or z.getRight() == self.__ward:
            y = z
        else:
            y = self.successor(z)

        if(y.getLeft() != self.__ward):
            x = y.getLeft()
        else:
            x = y.getRight()

        x.setFather(y.getFather())
        if(y.getFather() == self.__ward):
            self.__root = x
        else:
            if(y == y.getFather().getLeft()):
                y.getFather().setLeft(x)
            else:
                y.getFather().setRight(x)

        if(y != z):
            z.setKey(y.getKey())
            z.setData(y.getData())

        if(y.getColor() == 'black'):
            self.RBdeleteFixUP(x)

        self.__length -= 1
        self.wardFixUP()
        return 1
    
    def RBdeleteFixUP(self, x):

        while x != self.__root and x.getColor() == 'black':
            if(x == x.getFather().getLeft()):
                w = x.getFather().getRight()
                if(w.getColor() == 'red'):
                    w.setColor('black')
                    x.getFather().setColor('red')
                    self.rotationRR(x.getFather())
                    w = x.getFather().getRight()

                if w.getLeft().getColor() == 'black' and w.getRight().getColor() == 'black':
                    w.setColor('red')
                    x = x.getFather()
                else:
                    if(w.getRight().getColor() == 'black'):
                        w.getLeft().setColor('black')
                        w.setColor('red')
                        self.rotationLL(w)
                        w = x.getFather().getRight()

                    w.setColor(x.getFather().getColor())
                    x.getFather().setColor('black')
                    w.getRight().setColor('black')
                    self.rotationRR(x.getFather())
                    x = self.__root
                        
            elif(x == x.getFather().getRight()):
                w = x.getFather().getLeft()
                if(w.getColor() == 'red'):
                    w.setColor('black')
                    x.getFather().setColor('red')
                    self.rotationLL(x.getFather())
                    w = x.getFather().getLeft()

                if w.getLeft().getColor() == 'black' and w.getRight().getColor() == 'black':
                    w.setColor('red')
                    x = x.getFather()
                else:
                    if(w.getLeft().getColor() == 'black'):
                        w.getRight().setColor('black')
                        w.setColor('red')
                        self.rotationRR(w)
                        w = x.getFather().getLeft()

                    w.setColor(x.getFather().getColor())
                    x.getFather().setColor('black')
                    w.getLeft().setColor('black')
                    self.rotationLL(x.getFather())
                    x = self.__root                        

        x.setColor('black')

#################################################################
        
if(__name__ == '__main__'):
    tree = RBTree()
    from random import randint, choice
    lista = []
    limite = 10000
    print('Inserindo...')

    for x in range(limite):
        y = randint(0,limite**2)
        #if(y not in lista):
        lista.append(y)
        #print(y)
        tree.insert(y)
    
    print('Deletando...')
    for x in range(limite//2):
        y = choice(lista)
        lista.remove(y)
        #print('Deletando:',y)
        tree.delete(y)
    '''
    import pickle
    pickle.dump(tree, open('RBTree-DataBase.rbt', 'wb'))
    print(tree)
    #arvore = pickle.load(open('RBTree-DataBase.rbt', 'rb'))
    '''
