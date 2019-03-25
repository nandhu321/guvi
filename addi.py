n,q = map(int,input().split())
lis = list(map(int,input().split()))
stri = ""
for i in range(q):
    u,v = map(int,input().split())
    ans  = sum(lis[u-1:v])
    if(i == 0):
        stri = stri+str(ans)
    else:
        stri = stri+"\n"+str(ans)
print(stri)
