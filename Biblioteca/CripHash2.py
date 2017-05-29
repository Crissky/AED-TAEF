from Base42 import base42encode
#mini = 3574546132030870770399332670577487090810665965922351838949846024192
#maxi = 150130937545296572356771972164254457814047970568738777235893533016063

def cripHash(string):
    try:
        string = str(string)
    except:
        raise TypeError("Dados do tipo '%s' não podem ser criptografados."%(str(type(string))[17:-2] if "<class '__main__." in str(type(string)) else str(type(string))[8:-2]))

    if(string == ''):
        raise ValueError("String vazia não pode ser criptografada.")
            
    global count
    count = 0
    value = 0
    crip = ''
    mini = 3574546132030870770399332670577487090810665965922351838949846024192
    maxi = 150130937545296572356771972164254457814047970568738777235893533016063


    #for 1
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x+711)**len(string))

    if(value%2176782335 < mini):
        value = inject(value, string)

    crip += base42encode(value%maxi)

    for x in range(len(crip)-6, 0, -6):
        crip = crip[:x]+' '+crip[x:]
    
    return crip
    

def inject(value, string):
    global count
    count += count+7
    mini = 3574546132030870770399332670577487090810665965922351838949846024192
    maxi = 150130937545296572356771972164254457814047970568738777235893533016063
    injecting = value*(len(string)*count)
    
    if(injecting%maxi < mini):
        return inject(injecting, string)
    else:
        return injecting
