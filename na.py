#nandhu
s=[]
n,k=map(int,input().split())
s= [[abs(i-k),i]for i in [int(x) for x in input().split()]]
s.sort()
s=s[1:]
s=[i[1] for i in s[:3]]
print(*s)
