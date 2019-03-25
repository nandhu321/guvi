s=input()
b=[]
b.extend([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])
a=''.join(b)
print(a.strip('"\''))
