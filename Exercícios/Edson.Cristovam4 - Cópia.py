arq = open('3.in', 'r')
n = int(arq.readline())
parts = []
y = arq.readline()
parts = y.split()
        
for x in range(n-1):
    parts[x] = int(parts[x])

for x in range(1,n+1):
    if(x not in parts):
        print(x)
        break
