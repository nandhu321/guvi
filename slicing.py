s1=input()
s2=input()
l1=len(s1)
l2=len(s2)
c=l1-l2
for i in range(0,c+1):
    if(s2==s1[i:i+l2]):
        print(i)
