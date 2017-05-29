casos = input().split()
resposta = ''

def contador(n,v=0):
    global drinks, emp
    drinks += n
    if(n == 2):
        return contador(int((n+1)/3))
    if(n >= 3):
        if(n%3 != 0 and emp == 0):
            emp += 1
            return contador(int(n/3)+1)
        else:
            return contador(int(n/3))
        
    
for x in casos:
    drinks = 0
    emp = 0
    if(int(x)%3 == 1 or int(x) == 5):
        drinks = -1
    contador(int(x))
    resposta = resposta+' '+str(drinks)

print(resposta[1:])
