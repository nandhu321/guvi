count=0
s=input()
try:
    sa=int(s)
    while True:
        if(sa>=10):
            sa=sa/10
            count=count+1
        else:
            count=count+1
            break
    print(count)
except:
    print("Invalid Input")


        
