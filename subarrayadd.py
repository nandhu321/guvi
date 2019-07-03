
def subArray(arr, n): 
    l=[]
    sum1=0
    for i in range(0,n): 
        sum1=0
        for j in range(i,n):
            sum1=0
            for k in range(i,j+1): 
                sum1=sum1+arr[k]
            l.append(sum1)
    print(max(l))
g=int(input())
arr = list(map(int,input().split())) 
n = len(arr)
subArray(arr, n); 
