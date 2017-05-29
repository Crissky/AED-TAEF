arq = open('1.in', 'r')
v = arq.readline().split()
count, res = 0,0 #CONTADOR DE FIM E RESPOSTA
loops = [] #LISTA DE MULTIPLICADORES

while 1:
    x = v.pop(0) #RECEBE OS ARGUMENTOS
    if(x == 'INICIO'): #RECEBE INICIO E ADD 1 AO CONTADOR
        count += 1
    elif(x == 'LOOP'): #RECEBE LOOP E ADD 1 AO CONTADOR
        count += 1
        if(len(loops) == 0): #SE A LISTA ESTÁ VAZIA, ADD UM MULTIPLICADOR
            loops.append(int(v.pop(0)))
        else: #SE A LISTA CONTÉM ALGUM MULTIPLICADOR, ADD AO FIM DA LISTA O PRODUTO DO ÚLTIMO ITEM DA LISTA PELO VALOR DO LOOP ATUAL
            loops.append(int(v.pop(0))*loops[-1])
    elif(x == 'OP'): #RECEBE OPERADOR
        if(len(loops) == 0): #OPERADOR FORA DE LOOP, ADD OPERADOR A RESPOSTA
            res += int(v.pop(0))
        else: #OPERADOR EM LOOP, ADD O PRODUTO ENTRE OPERADOR E DO ÚLTIMO ITEM DA LISTA DE MULTIPLICADORES A RESPOSTA
            res += int(v.pop(0))*loops[-1]
    elif(x == 'FIM'):#RECEBE FIM
        count -= 1
        if(count == 0):#SE CONTADOR É ZERO, FIM DO WHILE
            break
        else:# SE CONTADOR É MAIOR QUE ZERO, FIM DE UM LOOP.
            loops.pop(-1)
print(res)
