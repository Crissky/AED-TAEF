def QSort(x,p,r):
    if(p < r):
        q = PQSort(x,p,r) #q[0] = i; q[1] = p; q[2] = r
        QSort(x, q[1],q[0]-1)
        QSort(x, q[0]+1,q[2])
        
    
def PQSort(x,p,r):
    y = x[r] #pivô
    i = p-1
    for j in range(p,r):
        if(x[j] <= y):
            i += 1
            x[i],x[j] = x[j],x[i]

    x[i+1],x[r] = x[r],x[i+1]
    return i+1,p,r #x[:i],x[i:]


entrada = input() #"Digite uma esqu$ncia numérica: "
#entrada = '09 08 07 05 04 02 10'
x = entrada.split(' ')
for y in range(len(x)):
    x[y] = int(x[y])
QSort(x,0,len(x)-1)
for y in range(len(x)-1):
    print(x[y], end=' ')
print(x[len(x)-1])



