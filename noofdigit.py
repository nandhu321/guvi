count=0
s=int(input())
while True:
    if(s>=10):
        s=s/10
        count=count+1
    else:
        count=count+1
        break
print(count)

        
