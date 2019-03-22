
a=input().split()
b=int(a[0])
c=int(a[1])
d=int(a[2])
if b%2==0:
    b=b//2
    c1=b//c
    d1=b//d
    
    f=0
    for i in range(c1+1):
        for j in range(d1+1):
           
            if (c*i+d*j)==b:
                f=1
    if f==0:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
