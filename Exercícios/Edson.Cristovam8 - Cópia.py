arq = open('1.in','r')
arq = arq.readline().split()
n,m = int(arq.pop(0)), int(arq.pop(0))
count = 0
lista = []
res = ''
for y in arq:
    for w in range(n):
        #print()
        for z in range(n-w):
            #print('w:',y[w], 'z:',y[w+z], end=' || ')
            if(y[w] > y[w+z]):
                count += 1
    lista.append(count)                
    #print(count)
    count = 0

for x in range(m):
    r = lista.index(min(lista))
    lista.pop(r)
    res += arq.pop(r) + '\n'

print(res[:-1])
    
