from Base42 import base42encode
#60466176  2176782335
#130691232 5489031743
def cripHash(string):
    try:
        string = str(string)
    except:
        raise TypeError("Dados do tipo '%s' não ser criptografados."%(str(type(string))[17:-2] if "<class '__main__." in str(type(string)) else str(type(string))[8:-2]))

    if(string == ''):
        raise ValueError("String vazia não pode ser criptografada.")
    
    global count
    count = 0
    value = 0
    crip = ''
    #for 1
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*(x+30233088)*len(string)

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += base42encode(value%5489031743)
    
    #for 2
    value = 0
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x+10077696+x)*len(string))

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += ' '+base42encode(value%5489031743)

    #for 3
    value = 0
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x*711 if x > 0 else 355)*len(string))

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += ' '+base42encode(value%5489031743)

    #for 4
    value = 0
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x*12345 if x > 0 else 54321)*len(string)//2)

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += ' '+base42encode(value%5489031743)

    #for 5
    value = 0
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x+x+42+x+x)*len(string)*711)

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += ' '+base42encode(value%5489031743)

    #for 6
    value = 0
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x+len(string)*224466)*len(string))

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += ' '+base42encode(value%5489031743)

    #for 7
    value = 0
    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x*x*x if x > 0 else 47)*len(string))

    if(value%5489031743 < 130691232):
        value = inject(value, string)

    crip += ' '+base42encode(value%5489031743)

    return crip

def inject(value, string):
    global count
    count += 7
    injecting = value*(len(string)*count)
    
    if(injecting%5489031743 < 130691232):
        return inject(injecting%5489031743, string)
    else:
        return injecting
    
