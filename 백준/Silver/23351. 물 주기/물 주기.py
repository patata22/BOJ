from collections import deque

n,k,a,b=map(int,input().split())
q=deque([k]*(n//a))
lose=0
answer=1

while True:
    q.append(q.popleft()+b)
    lose+=1
    if q[0]<=lose: break
    answer+=1

print(answer)