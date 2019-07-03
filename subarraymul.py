
def subArray(arr, n): 
    l=[]
    mul1=1
    for i in range(0,n): 
        mul1=1
        for j in range(i,n):
            mul1=1
            for k in range(i,j+1): 
                mul1=mul1*arr[k]
            l.append(mul1)
    print(max(l))
g=int(input())
arr = list(map(int,input().split())) 
n = len(arr)
subArray(arr, n); 
