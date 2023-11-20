from collections import deque

n,m=map(int,input().split())
number=tuple(map(int,input().split()))
M=9*m//10
if 9*m%10: M+=1

answer='NO'

count=[0]*(10**6+1)
q=deque()
for i in range(m):
    x=number[i]
    q.append(x)
    count[x]+=1
    if count[x]>=M: answer='YES'

for i in range(m,n):
    y=q.popleft()
    count[y]-=1
    x=number[i]
    count[x]+=1
    if count[x]>=M: answer='YES'
    q.append(x)
print(answer)
