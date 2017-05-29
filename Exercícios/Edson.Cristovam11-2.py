l = input().split()
m, n = int(l[0]), int(l[1])
res = 0

res += m-1

for x in range(m):
    res += n-1
    
print(res)
