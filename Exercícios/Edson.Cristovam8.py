arq = input().split()
n,m = int(arq.pop(0)), int(arq.pop(0))
count = 0
lista = []
res = ''
for y in arq:
    for w in range(n):
        for z in range(n-w):
            if(y[w] > y[w+z]):
                count += 1
    lista.append(count)                
    count = 0

for x in range(m):
    r = lista.index(min(lista))
    lista.pop(r)
    res += arq.pop(r) + '\n'

print(res[:-1])
    
