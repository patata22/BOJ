from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
            answer[i]=time[i]
    while q:
        now=q.popleft()
        for x in graph[now]:
            answer[x]=max(answer[now]+time[x], answer[x])
            indegree[x]-=1
            if not indegree[x]:
                q.append(x)
        

for _ in range(int(input())):
    n,k=map(int,input().split())
    time=[0]+list(map(int,input().split()))
    answer=[0]*(n+1)
    graph=[[] for i in range(n+1)]
    indegree=[0]*(n+1)
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1
    sol()
    print(answer[int(input())])
