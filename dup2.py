n=int(input())
lis=list(map(int,input().split()))
l=[]
a=[]
for i in range(0,n):
    for j in range(i+1,n):
        if(lis[i]==lis[j]) and lis[i] not in l:
            l.append(lis[i])
if(len(l)==0):
    print("unique")
else:
    a.append(str(l[0]))
    b=" ".join(a)
print(b)
