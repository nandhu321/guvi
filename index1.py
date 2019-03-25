n=int(input())
lis=list(map(int,input().split()))
l=[]
a=0
for i in range(0,n):
    if (lis[i]==a):
        l.append(str(a))
        b=" ".join(l)
        a=a+1
    else:
        a=a+1
if(len(l)==0):
    print("-1")
else:
    print(b.strip('"\''))
