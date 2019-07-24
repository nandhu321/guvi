from itertools import permutations 
  
n=int(input())
lis=list(map(int,input().split()))
perm = permutations(lis, n-3) 
l=[]
for i in perm: 
    l.append(i)
c=[]
sum=0
for i in range(len(l)):
    sum=0
    for j in range(0,n-3):
        sum=sum+l[i][j]
    c.append(sum)
    
print(max(c)) 
    
