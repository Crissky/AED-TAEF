arq = open('entrada2.txt','r')
ret1 = arq.readline()
ret2 = arq.readline()
arq.close()

#X0, Y0, X1, Y1 = (RET[0], RET[1], RET[2], RET[3])
ret1 = ret1.split()
ret2 = ret2.split()

#Comparando X
if (int(ret1[0]) < int(ret2[0])):
    if(int(ret2[0]) <= int(ret1[2])):
        x = 'true'
    else:
        x = 'false'
        
elif(int(ret1[0]) <= int(ret2[2])):
    x = 'true'

#Comparando Y
if(x == 'true'):
    if(int(ret1[1]) < int(ret2[1])):
        if(int(ret2[1]) <= int(ret1[3])):
            colide = '1'
        else:
            colide = '0'

    elif(int(ret1[1]) <= int(ret2[3])):
        colide = '1'
else:
    colide = '0'

arq = open('saída2.txt','w')
arq.write(colide)
arq.close()
