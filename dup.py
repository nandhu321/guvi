n=int(input())
lis=list(map(int,input().split()))
l=[]
for i in range(0,n):
    for j in range(i+1,n):
        if(lis[i]==lis[j]):
            l.append(str(lis[i]))
            b=' '.join(l)
print(b.strip('"\''))
