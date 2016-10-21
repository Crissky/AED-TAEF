from random import randint
h = [randint(10,99) for i in range(10)]

def BSort(x): #Bubble Sort
    for i in range(len(x)-1):
        for y in range(len(x)-1):
            if(x[y] > x[y+1]):
                x[y],x[y+1] = x[y+1],x[y]

def MSort(vector): #Merge Sort
    if len(vector)>1:
        mid = len(vector)//2
        left, right = vector[:mid], vector[mid:]

        MSort(left)
        MSort(right)

        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                vector[k]=left[i]
                i += 1
            else:
                vector[k]=right[j]
                j += 1
            k += 1

        while i < len(left):
            vector[k]=left[i]
            i += 1
            k += 1

        while j < len(right):
            vector[k]=right[j]
            j += 1
            k += 1

def HMax(x,c): #Heap Sort
    for y in range(int(c/2)-1,-1,-1):
        if(x[y] < x[y*2+1]):
            x[y],x[y*2+1] = x[y*2+1],x[y]
        if(y*2+2 <= c-1):
            if(x[y] < x[y*2+2]):
                x[y],x[y*2+2] = x[y*2+2],x[y]

def HSort(x): #Heap Sort
    HMax(x,len(x))
    for y in range(len(x)-1,0,-1):
        x[y],x[0] = x[0],x[y]
        HMax(x,y)

        
def QSort(x,p,r): #Quick Sort
    if(p < r):
        q = PQSort(x,p,r) #q[0] = i; q[1] = p; q[2] = r
        QSort(x, q[1],q[0]-1)
        QSort(x, q[0]+1,q[2])
        
    
def PQSort(x,p,r): #Quick Sort
    y = x[r] #pivô
    i = p-1
    for j in range(p,r):
        if(x[j] <= y):
            i += 1
            x[i],x[j] = x[j],x[i]

    x[i+1],x[r] = x[r],x[i+1]
    return i+1,p,r #x[:i],x[i:]

print(h)
#QSort(h,0,len(h)-1)
#HSort(h)
#BSort(h)
MSort(h)
print(h)
