d={}
for _ in range(5):
    x=int(input())
    if x not in d: d[x]=0
    d[x]+=1
for x in d:
    if d[x]%2==1: print(x)
