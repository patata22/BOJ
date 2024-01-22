import sys
input=sys.stdin.readline
from collections import deque

charToNum={'Baba':0}
numToChar={0:'Baba'}
unused=0
n=int(input())
graph=[[] for i in range(2*n)]
for _ in range(n):
    a,b=input().rstrip().split(' is ')
    if a not in charToNum:
        unused+=1
        charToNum[a]=unused
        numToChar[unused]=a
    if b not in charToNum:
        unused+=1
        charToNum[b]=unused
        numToChar[unused]=b
    a,b=charToNum[a], charToNum[b]
    graph[a].append(b)

q=deque()
q.append(0)
visited=[0]*(2*n)
while q:
    now=q.popleft()
    for to in graph[now]:
        if not visited[to]:
            visited[to]=1
            q.append(to)
answer=[]
for i in range(2*n):
    if visited[i]: answer.append(numToChar[i])
answer.sort()
print('\n'.join(answer))