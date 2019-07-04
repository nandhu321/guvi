c=input()
u=c.lower()
l=len(c)
j=0
for i in u:
    j=j+1
    y=u.count(i)
    if(u[j-1].isalpha()):
        if(y==1):
            print(u[j-1],end=" ")
