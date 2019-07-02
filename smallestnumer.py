m,n=map(int,input().split())
if(m>n):
    if(m%n==0):
        print(n)
elif(n>m):
    if(n%m==0):
        print(m)
else:
    print(m)
if(m%n!=0 and n%m!=0):
    print(m*n)

