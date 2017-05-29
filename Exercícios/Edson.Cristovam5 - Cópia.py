meses = [['JAN','MAR','MAI','JUL','AGO','OUT','DEZ'],["ABR","JUN","SET","NOV"],['FEV']]
dias = ["DOM","SEG","TER","QUA","QUI","SEX","SAB"]

arq = open('2.in','r')
n = int(arq.readline())
res = 0

for x in range(n):
    caso = arq.readline().split()
    if(caso[0] in meses[0]):
        y = 31
        #print(caso[0])
    elif(caso[0] in meses[1]):
        y = 30
        #print(caso[0])
    else:
        y = 28
        #print(caso[0])
    w = dias.index(caso[1])
    for z in range(y):
        dia = (w+z)%7
        #print(dias[dia])
        if(dias[dia] == "DOM" or dias[dia] == "SAB"):
            res += 1
            #print(dias[dia])
        
    print(res)
    res = 0
    
