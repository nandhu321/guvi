n=input()
l=len(n)
c=int(n)
sum1=0
rev=0
for i in range(0,l):
    f=c%10
    sum1=sum1+int(f)
    c=c/10
j=sum1
if(sum1<10):
    print("yes")
else:
    while (sum1!=0):
        g=int(sum1)%10
        rev=rev*10+g
        sum1=sum1//10
if(rev==j):
     print("YES")
else:
     print("NO")
   
    
