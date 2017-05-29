from math import sqrt

try:
    arq = open('Primos.txt', 'r+')
    alist = arq.readlines()
    primos = list(map(int, alist))
    alist = None
    i = primos[-1]
except:
    arq = open('Primos.txt', 'w')
    arq.write(str(2)+'\n')
    i = 2
    primos = [2]    

print('Iniciando apartir de',i, end='. ')
print('Que é o %dº número primo.' %(len(primos)))

while 1:
    i += 1
    if(i%2 == 0):
        continue

    root = sqrt(i)+1
    quest = True

    for x in primos:
        if(i%x == 0):
            quest = False
            break
        if(x > root):
            break
            
    if(quest):
        primos.append(i)#, print(i)
        arq.write(str(i)+'\n')
        
      

arq.close()
