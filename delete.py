n,k=map(str,input().split())
g=len(n)-int(k)
a=[]
for i in range(len(n)):
    f=n[i:i+g]
    if len(f)==g:
        a.append(int(f))
print(min(a))
