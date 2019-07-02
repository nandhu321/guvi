s,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
e,f=list(map(int,input().split()))
g,h=list(map(int,input().split()))
m=d-b
n=f-h
o=e-c
p=g-s
if (m==n==o==p):
    print("yes")
else:
    print("no")
    
