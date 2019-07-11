n=int(input())
l=[[]]
lis=list(map(int,input().split()))
for i in range(n+1):
    for j in range(i+1,n+1):
        l.append(lis[i:j])
l2=len(l)
l3=[]
for i in range(1,l2):
    c=len(l[i])
    mul=1
    for j in range(0,c):
        mul=mul*l[i][j]
    l3.append(mul)
print(abs(max(l3)))
