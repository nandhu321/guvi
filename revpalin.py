n=input()
n=list(map(int,g))
s=0
for i in n:
    s=s+int(i)
if(str(s)==str(s)[::-1]):
    print("YES")
else:
    print("NO")
