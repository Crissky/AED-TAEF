class NoHash:
    def __init__(self, idReal, data):
        self.__idReal = idReal
        self.__data = data

    def getID(self):
        return self.__idReal
    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def __str__(self):
        return str(self.__data)
    
class THash:
    def __init__(self, functionHash, length=1):
        self.__fHash = functionHash
        self.__table = [None]*length
        self.table2 = self.__table

    def __len__(self):
        return len(self.__table)

    def __str__(self):
        txt = '['
        for x in self.__table:
            if(x != None):
                txt += '['
                for y in x:
                    txt += str(y)+', '
                txt = txt[:-2]+'], '
            else:
                txt += str(None)+', '
                
        return txt[:-2]+']'
        
    def insert(self, idReal, data):
        if(self.search(idReal) == None):
            node = NoHash(idReal, data)
            idHash = self.__fHash(idReal)

            if(len(self.__table) <= idHash):
                self.__table = self.__table+[None]*(idHash - len(self.__table) + 1)
            if(self.__table[idHash] == None):
                self.__table[idHash] = [node]
            else:
                self.__table[idHash].append(node)
        else:
            self.update(idReal, data)

    def search(self, idReal):
        idHash = self.__fHash(idReal)

        if(idHash >= len(self.__table)):
            x = None
        else:
            x = self.__table[idHash]
            
        if(x != None):
            for y in x:
                if(y.getID() == idReal):
                    return y
        return None
        
    def delete(self, idReal):
        idHash = self.__fHash(idReal)

        if(idHash >= len(self.__table)):
            x = None
        else:
            x = self.__table[idHash]
        
        if(x != None):
            for y in range(len(x)):
                if(x[y].getID() == idReal):
                    del x[y]
                    if(len(x) == 0):
                        self.__table[idHash] = None
                    break

    def update(self, idReal, data):
        node = self.search(idReal)
        if(node != None):
            node.setData(data)

        
#from funcHash import *
#table = THash(funcaoHash,N)
table = THash(lambda x:x%100)
res = ''
#res2 = []

entrada = input().split('!!!')

for x in range(len(entrada)):
    comando = entrada[x][:entrada[x].find(' ')]
    entrada[x] = entrada[x].lstrip(comando+' ')

    if(comando == 'insert'):
        idReal = int(entrada[x][:entrada[x].find(' ')])
        entrada[x] = entrada[x][entrada[x].find(' ')+1:]
        table.insert(idReal, entrada[x])
        
    elif(comando == 'update'):
        idReal = int(entrada[x][:entrada[x].find(' ')])
        entrada[x] = entrada[x][entrada[x].find(' ')+1:]
        table.update(idReal, entrada[x])
        
    elif(comando == 'query'):
        idReal = int(entrada[x])
        res += str(table.search(idReal).getData())+"!!!"
        #res2.append(table.search(idReal).getData())
    elif(comando == 'delete'):
        idReal = int(entrada[x])
        table.delete(idReal)

print(res[:-3])
#print('!!!'.join(res2))

