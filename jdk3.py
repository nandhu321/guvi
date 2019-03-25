n,q = map(int,input().split())
lis = list(map(int,input().split()))
st = ""
for i in range(q):
    u,v = map(int,input().split())
    ans  = sum(lis[u-1:v])
    if(i == 0):
        st = st+str(ans)
    else:
        st = st+"\n"+str(ans)
print(st)
