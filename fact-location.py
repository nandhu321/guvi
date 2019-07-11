n=int(input())
lis=list(map(int,input().split()))
r=1
l=[]
for i in lis:
  r=r*i
for i in lis:
  l.append(r//i)
print(*l)
