m,n = map(int,input().split())
a = []
temp = list(map(int,input().split()))
a.append(sorted(temp))
if(len(temp) != n):
    m,n =n,m
for i in range(m-1):
    temp = list(map(int,input().split()))
    a.append(sorted(temp))
for i in range(n):
    for j in range(m-1):
        for k in range(j,m):
            if(a[j][i] > a[k][i]):
                a[j][i],a[k][i] = a[k][i],a[j][i]
for i in range(m):
    print(" ".join(map(str,a[i])))
