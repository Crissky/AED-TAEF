#arq = open('1.in','r')
#lista = arq.readline().split()
lista = input().split()
lista2, alunos, astr = {}, {}, ''

for x in range(0,len(lista),2): #Criando um Dicionário com as salas como chaves e o alunos como valores.
    if(lista[x+1] in lista2.keys()):
        lista2[lista[x+1]].append(lista[x])
    else:
        lista2[lista[x+1]] = [lista[x]]

    if(lista[x] not in alunos.keys()): #Criando um Dicionário com os alunos como chaves.
        alunos[lista[x]] = []

for x in alunos.keys(): #Adicionando ao Dicionário {alunos} os alunos que estudam junto com os alunos que são as chaves.
    for y in lista2.keys():
        if(x in lista2[y] and len(lista2[y]) > 1):
            for z in lista2[y]:
                if(z != x and z not in alunos[x]):
                    alunos[x].append(z)


for x in sorted([int(y) for y in alunos.keys()]): #For em todas as chaves de alunos em ordem para criar a string com a resposta.
    astr += str(x)+' '+str(len(alunos[str(x)]))+' '

print(astr[:-1])
