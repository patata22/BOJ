from collections import deque

n,k=map(int,input().split())
if n>=k:print(n-k)
else:
    maxnum=100000
    visited=[0 for i in range(100001)]
    def bfs(n):
        q=deque()
        q.append(n)
        while q:
            x= q.popleft()
            if x==k:return visited[x]
            for y in (x-1, x+1, x*2):
                if 0<=y<=maxnum and visited[y]==0:
                    visited[y]=visited[x]+1
                    q.append(y)
    print(bfs(n))