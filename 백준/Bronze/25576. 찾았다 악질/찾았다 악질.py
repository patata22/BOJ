n,m=map(int,input().split())
me=tuple(map(int,input().split()))

answer=0
for _ in range(n-1):
    temp = tuple(map(int,input().split()))
    total=0
    for i in range(m):
        total+=abs(me[i]-temp[i])
    if total>2000: answer+=1

if answer*2>=n-1: print('YES')
else: print('NO')
