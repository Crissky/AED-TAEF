meses = [['JAN','MAR','MAI','JUL','AGO','OUT','DEZ'],["ABR","JUN","SET","NOV"],['FEV']]
dias = ["DOM","SEG","TER","QUA","QUI","SEX","SAB"]
n = int(input())
res = 0

for x in range(n):
    caso = input().split()
    if(caso[0] in meses[0]):
        y = 31
    elif(caso[0] in meses[1]):
        y = 30
    else:
        y = 28
    w = dias.index(caso[1])
    for z in range(y):
        dia = (w+z)%7
        if(dias[dia] == "DOM" or dias[dia] == "SAB"):
            res += 1
    print(res)
    res = 0
    
