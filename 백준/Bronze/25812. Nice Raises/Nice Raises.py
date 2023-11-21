fix=0
dou=0
n,r=map(int,input().split())
for _ in range(n):
    x=int(input())
    if x>r: dou+=1
    elif x<r:fix+=1

if fix==dou:print(0)
elif fix>dou:print(1)
else: print(2)
