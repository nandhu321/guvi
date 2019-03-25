n=int(input())
lis=list(map(int,input().split()))
l=[]
a=[]
for i in range(0,n):
    for j in range(i+1,n):
        if(lis[i]==lis[j]) and lis[i] not in l:
            l.append(lis[i])
l.sort()
if(len(l)==0):
    print("unique")
else:
    for i in range(0,len(l)):
        a.append(str(l[i]))
        b=" ".join(a)
print(b)
