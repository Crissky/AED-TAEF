from random import randint

def CPFVerify(CPF): #Autentica CPF apartir dos digitos verificadores
    if(type(CPF) != str):
        return 0
    
    #CPF = CPF.replace('.','')
    #CPF = CPF.replace('-','')

    if(len(CPF) == 11 and CPF.isnumeric()):
        asum = 0
        multiplier = 10
        for x in range(len(CPF)-2):
            asum += int(CPF[x])*multiplier
            multiplier -= 1

        if (asum%11 < 2 and int(CPF[-2]) == 0) or (asum%11 >= 2 and int(CPF[-2]) == 11-(asum%11)):
            asum = 0
            multiplier = 11
            for x in range(len(CPF)-1):
                asum += int(CPF[x])*multiplier
                multiplier -= 1

            if(asum%11 < 2 and int(CPF[-1]) == 0) or (asum%11 >= 2 and int(CPF[-1]) == 11-(asum%11)):
                return 1
    return 0    

def CPFGenerator(CPF):
    if(type(CPF) != str):
        return 0
    
    #CPF = CPF.replace('.','')
    #CPF = CPF.replace('-','')

    if(len(CPF) == 9 and CPF.isnumeric()):
        asum = 0
        multiplier = 10
        for x in range(len(CPF)):
            asum += int(CPF[x])*multiplier
            multiplier -= 1

        if(asum%11 < 2):
            CPF += '0'
        else:
            CPF += str(11-asum%11)

        asum = 0
        multiplier = 11
        for x in range(len(CPF)):
            asum += int(CPF[x])*multiplier
            multiplier -= 1

        if(asum%11 < 2):
            CPF += '0'
        else:
            CPF += str(11-asum%11)

    return CPF #CPF[:3]+'.'+CPF[3:6]+'.'+CPF[6:-2]+'-'+CPF[-2:]

def CPFRandom():
    CPF = str(randint(0, 999999999)).rjust(9,'0')
    return CPFGenerator(CPF)
    
    
def ISBNVerify(ISBN):
    if(type(ISBN) != str):
       return 0
       
    #ISBN = ISBN.replace('-','')

    if(len(ISBN) == 13 and ISBN.isnumeric()):
        asum = 0
        for x in range(len(ISBN)-1):
            if(x%2 == 0):
                asum += int(ISBN[x])*1
            else:
                asum += int(ISBN[x])*3
                
        if (10-asum%10 == 10 and int(ISBN[-1]) == 0):
            return 1
        elif(10-asum%10 == int(ISBN[-1])):
            return 1
            
    return 0

def ISBNGenerator(ISBN):
    if(type(ISBN) != str):
       return 0
       
    #ISBN = ISBN.replace('-','')

    if(len(ISBN) == 12 and ISBN.isnumeric()):
        asum = 0
        for x in range(len(ISBN)):
            if(x%2 == 0):
                asum += int(ISBN[x])*1
            else:
                asum += int(ISBN[x])*3
    if(10-asum%10 == 10):
        ISBN += '0'
    else:
        ISBN += str(10-asum%10)
    return ISBN

def ISBNRandom():
    ISBN = str(randint(0, 999999999999)).rjust(12,'0')
    return ISBNGenerator(ISBN)

if(__name__ == '__main__'):
    limite = 0
    '''
    arq = open('CPFs.txt', 'w')
    for x in range(1000000000):
        CPF = CPFGenerator(str(x).rjust(9,'0'))
        if(CPF != 0):
            arq.write(CPF+'\n')
    arq.close()
    
    '''
    print('CPFs:')

    for x in range(limite):
        CPF = CPFRandom()
        vCPF = CPFVerify(CPF)
        if(vCPF == 0):
            print('\n', CPF, vCPF)
        #else:
        #    print(CPF, end=', ')

    print('\nISBNs:')
    
    for x in range(limite):
        ISBN = ISBNRandom()
        vISBN = ISBNVerify(ISBN)
        if(vISBN == 0):
            print('\n', ISBN, vISBN)
        #else:
        #    print(ISBN, end=', ')
            
    '''
    print('CPFs:')
    
    for x in range(limite):
        pCPF = str(randint(100000000, 999999999))
        CPF = CPFGenerator(pCPF)
        vCPF = CPFVerify(CPF)
        if(vCPF == 0):
            print(pCPF, CPF, vCPF)

    print('\nISBNs:')
    for x in range(limite):
        pISBN = str(randint(100000000000, 999999999999))
        ISBN = ISBNGenerator(pISBN)
        vISBN = ISBNVerify(ISBN)
        if(vISBN == 0):
            print(pISBN, ISBN, vISBN)
    '''
