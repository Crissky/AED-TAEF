n = int(input())

mat = []

#Montando Matriz
for x in range(n):
    y = input()
    mat.append(y.split())
    #Transformando de Str para Int
    for y in range(int(n)):
        mat[x][y] = int(mat[x][y])

res = sum(mat[0])
com = 0

while 1:
    #Somando Linhas
    for x in range(n):
        com = sum(mat[x])
        if(com != res):
            break
    if(com != res):
        break

    #Somando Colunas
    for x in range(n):
        com = 0
        for y in range(n):
            com += mat[y][x]
        if(com != res):
            break
    if(com != res):
        break

    #Somando Diagonal 1
    com = 0
    for x in range(n):
        com += mat[x][x]
    if(com != res):
        break

    #Somando Diagonal 2
    com = 0
    for x in range(n):
        #print("x:",x,'y:',n-1-x)
        com += mat[x][((n-1)-x)]

    break
if(com != res):
    print(-1)
else:
    print(com)
