n=int(input())
lis=list(map(int,input().split()))
lis.reverse()
l=len(lis)
for i in range(0,l):
    if(l-1!=i):
        print(lis[i],end="->")
    else:
        print(lis[i])
