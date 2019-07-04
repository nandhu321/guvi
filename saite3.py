m,n=map(int,input().split())
lis=list(map(int,input().split()))
l=len(lis)
count=0
for i in range(0,l):
    if(n==lis[i]):
        count=count+1
    else:
        continue
if(count==0):
    print("No")
else:
    print("Yes")
