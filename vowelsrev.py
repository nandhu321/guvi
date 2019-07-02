m=int(input())
c=input()
l=len(c)
s=[]
for i in range(0,l):
    if(c[i]=='a' or c[i]=='e' or c[i]=='o' or c[i]=='u' or c[i]=='i'):
        continue
    else:
        s.append(c[i])
b=''.join(s)
print(b[::-1])
