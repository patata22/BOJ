from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    answer=[]
    for i in range(1,n+1):
        if indegree[i]==0: q.append(i)
    for i in range(n):
        if not q: return 0
        now = q.popleft()
        answer.append(now)
        for x in graph[now]:
            indegree[x]-=1
            if indegree[x]==0:q.append(x)
    return answer
        
        


n,m=map(int,input().split())
indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]


for _ in range(m):
    temp=list(map(int,input().split()))
    for i in range(1,temp[0]):
        a,b=temp[i],temp[i+1]
        graph[a].append(b)
        indegree[b]+=1

temp = sol()
if temp==0: print(0)
else:
    for x in temp: print(x)
