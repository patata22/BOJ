from collections import deque

def sol():
    q=deque()
    answer=0
    for i in range(n):
        if indegree[i]==0:
            q.append(i)
            answer+=1
    while q:
        now=q.popleft()
        indegree[nxt[now]]-=1
        if indegree[nxt[now]]==0:
            q.append((nxt[now]))
            answer+=1
    return answer

for _ in range(int(input())):
    n=int(input())
    nxt=list(map(lambda x: int(x)-1, input().split()))
    indegree=[0]*n
    for i in range(n):
        indegree[nxt[i]]+=1
    print(sol())

