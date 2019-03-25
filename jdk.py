
n = int(input(""))
lis = list(map(int,input().split()))
lis = sorted(lis,reverse = True)
ans =[]
for i in lis:
    x = str(bin(i))
    c = 0
    for j in x:
        if(j == '1'):
            c+=1
    ans.append(c)
for i in range(n):
    for j in range(i,n):
        if(ans[i]<ans[j]):
            ans[i],ans[j] = ans[j],ans[i]
            lis[i],lis[j] = lis[j],lis[i]
print("\n".join(map(str,lis)))
