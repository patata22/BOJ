from collections import deque
import sys
input=sys.stdin.readline

def sol(start):
    q=deque()
    visited=[(-1,-1)]*(n+1)
    for x in start:
        visited[x]=(0,x)
        q.append((x,x))
    t=0
    while q:
        t+=1
        if t>k: return False
        for _ in range(len(q)):
            now,origin=q.popleft()
            for to in graph[now]:
                if visited[to][0]==-1:
                    visited[to]=(t,origin)
                    q.append((to,origin))
                else:
                    if visited[to][1]!=origin:
                        if visited[to][0]+t<=k: return True
    return False

n,m,k=map(int,input().split())
w=int(input())
numToName={}
nameToNum={}

for _ in range(w):
    a,b=input().split()
    numToName[int(a)]=b
    if b not in nameToNum: nameToNum[b]=[]
    nameToNum[b].append(int(a))
    

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer='so sad'
for x in nameToNum:
    now=nameToNum[x]
    if len(now)<2: continue
    result=sol(now)
    if result:
        answer='POWERFUL CODING JungHwan'
        break

print(answer)
