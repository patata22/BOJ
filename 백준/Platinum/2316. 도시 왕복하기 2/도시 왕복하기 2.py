from collections import deque
import sys
input=sys.stdin.readline

START=401
END=2

def sol():
    total=0
    while True:
        q=deque()
        prev=[-1]*801
        q.append(START)
        while q:
            now=q.popleft()
            for to in graph[now]:
                if prev[to]<0 and capa[now][to]>0:
                    prev[to]=now
                    q.append(to)
                if prev[END]>0: break
        if prev[END]==-1: break
        
        total+=1
        now=END
        while now!=START:
            capa[prev[now]][now]-=1
            capa[now][prev[now]]+=1
            now=prev[now]
    return total        

n,m=map(int,input().split())
graph=[[] for i in range(801)]
capa=[[0]*801 for i in range(801)]    

for i in range(1,n+1):
    graph[i].append(i+400)
    capa[i][i+400]=1
    
for i in range(m):
    a,b=map(int,input().split())
    graph[a+400].append(b)
    graph[b].append(a+400)
    capa[a+400][b]+=1

    graph[b+400].append(a)
    graph[a].append(b+400)
    capa[b+400][a]+=1
print(sol())
