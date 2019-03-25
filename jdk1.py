
n,k = map(int,input("").split())
lis = list(map(int,input().split()))
flag=0 
for i in range(n-1):
    for j in range(i+1,n):
        if(lis[i] + lis[j] == k):
            flag= 1
if(flag== 1):
    print("yes")
else:
    print("no")
