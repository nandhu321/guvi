
n=int(input())
lis=list(map(int,input().split()))
lis.sort()
lis.reverse()
ans=0
for i in range(0,n):
    ans=ans+lis[i]
if(ans!=0):
    l=[]
    for i in range(0,n):
        l.append(str(lis[i]))
        b=''.join(l)
    print(b.strip('"\''))
else:
    print("0")
