m,n=map(int,input().split())
lis=list(map(int,input().split()))
c=len(lis)
for i in range(0,n):
    t=lis[c-1]
    for j in range(c-1,-1,-1):
        lis[j]=lis[j-1]
    lis[0]=t
for i in range(0,c):
    print(lis[i],end=" ")
