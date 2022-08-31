from collections import deque

def sol():
    q=deque()
    for i in range(cnt):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        for x in graph[now]:
            indegree[x]-=1
            blood[x]+=0.5*blood[now]
            if indegree[x]==0:
                q.append(x)

n,m=map(int,input().split())
start=input()
trans={}
trans[start]=0
cnt=1
tree=[tuple(list(input().split())) for i in range(n)]
for t in tree:
    for x in t:
        if x not in trans:
            trans[x]=cnt
            cnt+=1
indegree=[0]*cnt
graph=[[] for i in range(cnt)]
for a,b,c in tree:
    A,B,C = trans[a], trans[b], trans[c]
    graph[B].append(A)
    graph[C].append(A)
    indegree[A]+=2
blood={}
blood[0]=1
for i in range(1,cnt):
    blood[i]=0
sol()
answer=0
maxblood=0
for _ in range(m):
    x=input()
    if x not in trans: continue
    elif blood[trans[x]]>maxblood:
        maxblood=blood[trans[x]]
        answer=x
print(answer)