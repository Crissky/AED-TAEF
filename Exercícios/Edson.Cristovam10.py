lista = input().split()
ent = int(lista.pop(0))
res, stop = 0,0

if(len(lista)> 0):
    x = int(lista.pop(0))
else:
    x = ent
    
while (stop <= ent):
    if(len(lista)> 0):
        if(x < stop):
            print('entrou stop:',stop, 'x',x)
            x = int(lista.pop(0))
    else:
        if(x < stop):
            x = ent
    print('stop:',stop, 'x',x)
    
    if(x < stop+3):
        stop += 3
        if(stop < ent):
            res += 1
        else:
            break
    else:
        stop += 5
        if(stop < ent):
            res += 1
    print('stop:',stop)
print(res)
