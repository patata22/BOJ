c={}
for x in list(input()):
    if x not in c: c[x]=1
    else: c[x]+=1

odd=True
even=True

for x in c:
    if c[x]%2==0:
        odd=False
    else: even=False

if not odd and not even: print('0/1')
elif odd: print(1)
else:print(0)
