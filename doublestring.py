n=input()
a=0
for i in range(len(n)):
    if n[:i]==n[i+1:]:
        a=0
        break
    else:
        a=1
if a==0:
    print("YES")
else:
    print("NO")
