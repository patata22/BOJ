from collections import deque

a,b=map(int,input().split())
answer=0
q=deque()
q.append(4)
q.append(7)
while q:
    now = q.popleft()
    if a<=now<=b:
        answer+=1
    if now>b: break
    q.append(10*now+4)
    q.append(10*now+7)
print(answer)
