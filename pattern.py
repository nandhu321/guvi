def toString(List): 
    return ''.join(List) 
 
def permute(a, l, r): 
    if l==r: 
        print(toString(a)) 
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]
u=int(input())
l="{}"
b=[]
for i in range(0,u):
    b.append(l)
n = len(b)
c="".join(b)
a=list(c)
permute(a,1,n) 
