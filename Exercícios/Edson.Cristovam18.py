class Noh:
    def __init__(self, key, data):
        self.__key = key
        self.__data = data

    def getKey(self):
        return self.__key
    def getData(self):
        return self.__data

    def setKey(self, key):
        self.__key = key
    def setData(self, data):
        self.__data = data

    def __str__(self):
        return str(self.__data)

class FullBinaryTree:
    def __init__(self, height):
        self.__tree = [None]*((2**height)-1)
        self.__txt = ''
        
    def __len__(self):
        return len(self.__tree)
    def __str__(self):
        #return str(self.__tree)
        self.__txt = '['
        for x in self.__tree:
            self.__txt += str(x)+', '

        return self.__txt[:-2]+']'

    def insert(self, key, data):
        node = Noh(key, data)
        i = 0
        while i < len(self.__tree):
            #print('indice',i, 'key',key)
            if(self.__tree[i] == None):
                self.__tree[i] = node
                return 1
            else:
                if(node.getKey() <= self.__tree[i].getKey()):
                    i = (i*2)+1
                else:
                    i = (i*2)+2
        return 0

    def search(self, key):
        i = 0
        h = 1
        while i < len(self.__tree):
            if(self.__tree[i].getKey() == key):
                return self.__tree[i], h, i
            else:
                if(key <= self.__tree[i].getKey()):
                    i = (i*2)+1
                else:
                    i = (i*2)+2
                h += 1

        return None

    def walk(self, value):
        if(value == '-1'):
            self.preOrder()
        elif(value == '0'):
            self.inOrder()
        elif(value == '1'):
            self.posOrder()

        return self.__txt
    
    def preOrder(self, node=0):
        if(node == 0):
            self.__txt = ''
            if(self.__tree[node] == None):
                return 0
                
        if(node < len(self.__tree) and self.__tree[node] != None):
            self.__txt += str(self.__tree[node].getKey())+' '
            self.preOrder((node*2)+1)
            self.preOrder((node*2)+2)


    def inOrder(self, node=0):
            if(node == 0):
                self.__txt = ''
                if(self.__tree[node] == None):
                    return 0
                    
            if(node < len(self.__tree) and self.__tree[node] != None):
                self.inOrder((node*2)+1)
                self.__txt += str(self.__tree[node].getKey())+' '
                self.inOrder((node*2)+2)


    def posOrder(self, node=0):
        if(node == 0):
            self.__txt = ''
            if(self.__tree[node] == None):
                return 0
                
        if(node < len(self.__tree) and self.__tree[node] != None):
            self.posOrder((node*2)+1)
            self.posOrder((node*2)+2)
            self.__txt += str(self.__tree[node].getKey())+' '



#arq = open('3.in', 'r')
#entrada = arq.read().split('!!!')
entrada = input().split('!!!')

tree = FullBinaryTree(int(entrada.pop(0)))
res = ''

for x in range(len(tree)):
    key = int(entrada[x][:entrada[x].index(' ')])
    data = entrada[x][entrada[x].index(' ')+1:]
    tree.insert(key, data)

print(tree.walk(entrada[-1]))
