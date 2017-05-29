arq = open('1.in','r')
lista = arq.readline().split()
#lista = input().split()
lista2, turmas, grupos, inter, res, maior = [], [], [], [], [0], 0

while(len(lista) > 1):
    lista2.append([int(lista.pop(0)),int(lista.pop(0))])

for x in lista2:
    if(x[1] not in turmas):
        turmas.append(x[1])
        
for x in range(len(turmas)):
    grupos.append([])
    for y in lista2:
        if(y[1] == turmas[x]):
            grupos[x].append(y[0])

for x in range(len(grupos)-1):
    for y in range(x+1,len(grupos)):
        if(len((list(set(grupos[x]) & set(grupos[y])))) > 1):
            inter.append(list(set(grupos[x]) & set(grupos[y])))

for x in inter:
    z = inter.count(x)
    if(z > maior):
        res = x
        maior = z

print(' '.join([str(x) for x in res]))
