n=int(input())
s="kabali"
l=[]
count=0
for i in range(0,n):
    c=input()
    l.append(c)
for i in range(0,n):
    if(sorted(s)==sorted(l[i])):
        count=count+1
print(count)
    
