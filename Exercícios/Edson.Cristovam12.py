#arq = open('5.in','r')
#lista = arq.readline().split()
lista = input().split()
lista2, familia, familia2 = [],[],[]
del lista[:2]#lista.pop(0), lista.pop(0)
while (len(lista) > 0):
    lista2.append([int(lista.pop(0)),int(lista.pop(0))])
    
for x in range(len(lista2)):
    for y in range(len(lista2)):
        if(lista2[x][0] in lista2[y]):
            if(lista2[y][0] not in familia):
                familia.append(lista2[y][0])
            if(lista2[y][1] not in familia):
                familia.append(lista2[y][1])
        elif(lista2[x][1] in lista2[y]):
            if(lista2[y][0] not in familia):
                familia.append(lista2[y][0])
            if(lista2[y][1] not in familia):
                familia.append(lista2[y][1])
    #print(familia)
    case = False
    for i in familia:
        for j in range(len(familia2)):
            if(i in familia2[j]):
                case = True
                break
        if(case):
            break
        
    if(case):
        familia2[j] = familia2[j] + familia
    else:
        familia2.append(familia)
    #print(familia, familia2)
    familia = []

print(len(familia2))
familia3 = []

for x in range(len(familia2)):
    familia3.append([])
    for y in range(len(familia2[x])):
        if(familia2[x][y] not in familia3[x]):
            familia3[x].append(familia2[x][y])

#print(lista2)
#print(familia3)
