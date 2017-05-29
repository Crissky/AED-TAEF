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

    def __len__(self):
        return len(self.__tree)
    def __str__(self):
        #return str(self.__tree)
        txt = '['
        for x in self.__tree:
            txt += str(x)+', '

        return txt[:-2]+']'

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



#arq = open('1.in', 'r')
#entrada = arq.read().split('!!!')
entrada = input().split('!!!')

tree = FullBinaryTree(int(entrada.pop(0)))
res = ''

for x in range(len(tree)):
    key = int(entrada[x][:entrada[x].index(' ')])
    data = entrada[x][entrada[x].index(' ')+1:]
    tree.insert(key, data)

for y in range(len(tree), len(entrada)):
    #print(y)
    atuple = tree.search(int(entrada[y]))
    #print(atuple)
    if(atuple != None):
        res += str(atuple[1])+' '+str(atuple[2])+'!!!'
    else:
        res += '0!!!'

print(res[:-3])
