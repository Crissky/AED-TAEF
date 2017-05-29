#arq = open('2.in','r')
#lista = arq.readline().split()
lista = input().split()
lista2, turmas, grupos, res, alunos, astr = [], [], [], [], [], ''

while(len(lista) > 1): #Cria lista com pares [Matrícula do aluno, ID da Sala].
    lista2.append([int(lista.pop(0)),int(lista.pop(0))])

for x in lista2: #Cria uma lista com todas as salas.
    if(x[1] not in turmas):
        turmas.append(x[1])

for x in range(len(turmas)): #Cria uma lista com todos os [alunos em suas respectivas salas], as salas estão na mesma ordem que a lista TURMAS
    grupos.append([])
    for y in lista2:
        if(y[1] == turmas[x]):
            grupos[x].append(y[0])
    grupos[x].sort()

for x in grupos: #Cria uma lista com todos os alunos
    for y in x:
        if(y not in alunos):
            alunos.append(y)

alunos.sort()

for x in range(len(alunos)): #Cria uma lista com [todos os alunos] que cursam alguma disciplina com os alunos da lista ALUNOS. Obedecendo a ordem da lista ALUNOS.
    res.append([])
    for y in grupos:
        if(alunos[x] in y and len(y) > 1):
            for z in y:
                if(z != alunos[x] and z not in res[x]):
                    res[x].append(z)

for x in range(len(res)): #Concatena a 'Matrícula do aluno' com a "Quantidade de Amigos que estudam junto a ele"
    astr += str(alunos[x])+' '+str(len(res[x]))+' '

print(astr[:-1])
