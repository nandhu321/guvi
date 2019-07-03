l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
s=input()
la=len(s)
count=0
for i in range(0,la):
    if s[i] in l:
        count=count+1
if(count==0):
    print("yes")
else:
    print("no")
