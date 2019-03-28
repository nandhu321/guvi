n,k = map(int,input().split())
a= []
s = str(n)
for i in range(k):
    first = i
    last = len(s)-k+i
    x = s[first:last]
    a.append(x)
print(min(a))
