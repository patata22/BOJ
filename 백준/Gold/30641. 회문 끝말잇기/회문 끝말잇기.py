DIV=10**9+7

l,u=map(int,input().split())
cnt=0
total=0
if l<=1<=u:
    cnt+=1
    total+=1
if l<=2<=u:
    cnt+=1
    total+=1
now=1
for i in range(3,u+1):
    if i%2: now=(now*26)%DIV
    if l<=i:total+=now
if cnt%2: print('H')
else: print('A')
print(total%DIV)