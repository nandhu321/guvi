
n= int(input())
d=n
s=0
while(n>0):
    r=int(n%10)
    s=s*10+r
    n=int(n/10)
print(s)
