def iseven(x):
    if x%2==0:
        a=0
    else:
        a=1
    return a
b=[]
n=int(input())
l=[ int(i) for i in input().split()]
for j in range(0,len(l)):
    if iseven(j)==0 and iseven(l[j])==1:
        b.append(l[j])
    elif iseven(j)==1 and iseven(l[j])==0:
        b.append(l[j])
for v in range(0,len(b)):
    if v==0:
        print(b[v],end="")
    else:
        print("",b[v],end="")
    
