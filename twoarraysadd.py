a=input().split()
k=int(a[1])
c=0
lis=list(map(int,input().split()))
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]+lis[j]==k:
            c=1
            break
if c==1:
    print('YES')
else:
    print('NO')
