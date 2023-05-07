from collections import deque
import sys
input=sys.stdin.readline

q=deque()
answer=0
back=0
for _ in range(int(input())):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        q.append(temp[1])
        if len(q)>answer:
            answer=len(q)
            back=q[-1]
        elif len(q)==answer and back>q[-1]:
            back=q[-1]
    else: q.popleft()

print(answer,back)
