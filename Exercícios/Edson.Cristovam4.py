n = int(input())
parts = input().split()

for x in range(n-1):
    parts[x] = int(parts[x])

for x in range(1,n+1):
    if(x not in parts):
        print(x)
        break
