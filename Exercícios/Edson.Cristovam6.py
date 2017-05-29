#casos = input().split()
casos = '8 5 19 52 18 54 55 56 13'.split()
respostas = ''
def contador(n, v=0):
    global drinks, emp
    t = n+v
    #print('n:',n, 'v:', v, 't:',t)
    #print('Drinks:', drinks, 'Add:', n)

    #CASO BASE
    if(t == 1):
        drinks += 1
    #CASO BASE
    elif(t == 2):
        if(emp == 0):
            drinks += 3
        else:
            drinks += 2
    #CASO BASE
    #elif(t == 3):
    #    drinks += n+1

    #CASO BASE
    elif(t == 4):
        if(emp == 0):
            drinks += n+1+1
        else:
            drinks += n+1
    #CASO BASE
    #elif(t == 5):
    #    if(n == 5):
    #        drinks += 7
    #    else:
    #        if(emp == 0):
    #            drinks += n+1+1
    #        else:
    #            drinks += n+1
    
    #RECURSÃO
    elif(t%3 == 2):
        drinks += n
        if(emp == 0):
            emp +=1
            t += 1
            contador(t//3, t%3)
        else:
            contador(t//3, t%3)
    else:
        drinks += n
        contador(t//3, t%3)

        
for x in casos:
    x = int(x)
    drinks, emp = 0,0
    contador(x)
    respostas = respostas+' '+ str(drinks)
print(respostas[1:])
