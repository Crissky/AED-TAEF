lista = input().split()
ent = int(lista.pop(0))
res, stop = 0,0

if(len(lista)> 0):
    x = int(lista.pop(0))
else:
    x = ent
    
while (stop <= ent):
    while(x < stop):
        if(len(lista)> 0):
            x = int(lista.pop(0))
        else:
            if(x < stop):
                x = ent
    
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
            
print(res)
