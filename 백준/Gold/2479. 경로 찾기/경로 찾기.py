import sys
input=sys.stdin.readline
from collections import deque

def isConnect(a,b):
    diff=0
    for i in range(k):
        if a[i]!=b[i]:diff+=1
    return diff==1

def sol():
    q=deque()
    q.append(s)
    visited[s]=1
    while q:
        now=q.popleft()
        if now==e:
            answer=[]
            now=e
            while now!=-1:
                answer.append(now+1)
                now=prev[now]
            return answer[::-1]
            
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                prev[to]=now
                q.append(to)
    return [-1]

n,k=map(int,input().split())
number=[input().rstrip() for i in range(n)]
graph=[[] for i in range(n+1)]
for i in range(n):
    for j in range(i+1,n):
        if isConnect(number[i],number[j]):
            graph[i].append(j)
            graph[j].append(i)

visited=[0]*n
prev=[-1]*n

s,e=map(int,input().split())
s-=1
e-=1

print(*sol())
