from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    q.append(0)
    visited=[0]*(n+1)
    visited[0]=1
    while q:
        now=q.popleft()
        if now==n: return 1
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append(to)
    return 0
        
original=input().rstrip()
word=set()
for tt in range(int(input())):
    word.add(input().rstrip())
n=len(original)
graph=[[] for i in range(n)]

for i in range(n):
    for j in range(i,n):
        if original[i:j+1] in word:
            graph[i].append(j+1)
    
print(sol())
