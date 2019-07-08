from itertools import permutations
n=input()
perms = [''.join(p) for p in permutations(n)]
l= len(perms)
c=[]
b=[]
coun=0
for i in range(1,l):
    if(int(n)<int(perms[i])):
        p=int(perms[i])-int(n)
        c.append(p)
        b.append(perms[i])
        coun=coun+1
if(coun>0):
    print(min(b))
else:
    print("impossible")
    
