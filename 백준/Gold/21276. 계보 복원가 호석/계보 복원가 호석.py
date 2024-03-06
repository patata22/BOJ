from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    anc=[]
    pre=[[] for i in range(n)]
    for i in range(n):
        if not indegree[i]:
            anc.append(numToName[i])
            q.append(i)
    while q:
        now=q.popleft()
        for to in graph[now]:
            indegree[to]-=1
            if not indegree[to]:
                pre[now].append(numToName[to])
                q.append(to)
    anc.sort()
    print(len(anc))
    print(*anc)
    
    for i in range(n):
        pre[i].sort()
        print(numToName[i], len(pre[i]), *pre[i])
    
n=int(input())
names=input().rstrip().split()
names.sort()

unused=0
nameToNum={}
numToName={}
for x in names:
    nameToNum[x]=unused
    numToName[unused]=x
    unused+=1

indegree=[0]*n
graph=[[] for i in range(n)]
for _ in range(int(input())):
    a,b=map(lambda x: nameToNum[x], input().rstrip().split())
    graph[b].append(a)
    indegree[a]+=1

sol()
