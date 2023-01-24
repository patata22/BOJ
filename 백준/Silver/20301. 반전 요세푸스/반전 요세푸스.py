from collections import deque

def left():
    for _ in range(k-1):
        q.appendleft(q.pop())
    answer.append(q.pop())

def right():
    for _ in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())
    
n,k,m=map(int,input().split())
q=deque([i for i in range(1,n+1)])
answer=[]
C=1
count=0
while q:
    if C: right()
    else: left()
    count+=1
    if count%m==0: C=1-C

print(*answer, sep="\n")
