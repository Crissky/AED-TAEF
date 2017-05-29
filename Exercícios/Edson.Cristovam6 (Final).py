casos = input().split()
respostas = ''
def contador(n, v=0):
    global drinks, emp
    t = n+v
    #CASO BASE
    if(t == 1):
        drinks += 1
    #CASO BASE
    elif(t == 2):
        if(emp == 0):
            drinks += n+1
        else:
            drinks += n
    #CASO BASE
    elif(t == 4):
        if(emp == 0):
            drinks += n+1+1
        else:
            drinks += n+1
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
