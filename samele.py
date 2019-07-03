m,n=map(int,input().split())
a,b=map(int,input().split())
s,d=map(int,input().split())
if(m==a==s):
    print("yes")
elif(n==b==d):
    print("yes")
elif(m==n and a==b and s==d):
    print("yes")
else:
    print("no")
