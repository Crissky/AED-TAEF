arq = open('3.in', 'r')
v = arq.readline().split()
pilha = [0]
v.pop(0),v.pop()

while (len(v) > 0):
    x = v.pop(0)
    if(x == 'LOOP'):
        pilha.append(int(v.pop(0)))
        pilha.append(0)
    if(x == 'OP'):
        pilha.append(int(v.pop(0)) + pilha.pop())
    if(x == 'FIM'):
        pilha.append((pilha.pop()*pilha.pop())+pilha.pop())

print(pilha[0])
