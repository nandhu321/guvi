num,k = map(int,input().split())
res= []
s = str(num)
for i in range(k):
    first = i
    last = len(s)-k+i
    x = s[first:last]
    res.append(x)
print(min(res))
