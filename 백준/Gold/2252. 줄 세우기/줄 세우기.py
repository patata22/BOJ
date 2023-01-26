from collections import deque
import sys
input=sys.stdin.readline

adj = [[] for _ in range(32001)]
deg = [0 for _ in range(32001)]
n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    deg[b] += 1

q = deque()
for i in range(1, n+1):
    if deg[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end = ' ')
    for nxt in adj[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)
