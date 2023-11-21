even=0
odd=0

count={}
for x in input():
    if x not in count:
        count[x]=1
    else:count[x]+=1
for x in count:
    if count[x]%2:odd=1
    else: even=1
if even and odd: print(2)
elif even: print(0)
else: print(1)
