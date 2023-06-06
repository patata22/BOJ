from collections import deque

def sol(depth):
    global answer
    if depth==n:
        count=bfs()
        if count==2:
            total=0
            for i in range(n):
                if used[i]: total+=number[i]
                else: total-=number[i]
            answer=min(answer,abs(total))
        return
            
    used[depth]=1
    sol(depth+1)
    used[depth]=0
    sol(depth+1)

def bfs():
    count=0
    visited=[0]*n
    for i in range(n):
        if not visited[i]:
            count+=1
            q=deque()
            q.append(i)
            visited[i]=1
            while q:
                now=q.popleft()
                for to in graph[now]:
                    if not visited[to] and used[now]==used[to]:
                        visited[to]=1
                        q.append(to)

    return count

n=int(input())
number=tuple(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(n):
    graph[i]=list(map(lambda x: int(x)-1,input().split()))[1:]
answer=float('inf')
used=[0]*n
sol(0)
print(-1) if answer==float('inf') else print(answer) 
