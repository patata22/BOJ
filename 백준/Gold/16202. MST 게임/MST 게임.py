import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b: p[b]=a

def kruskal(k):
    total=0
    cnt=0
    for i in range(k,m):
        a,b,c=graph[i]
        if find(a)!=find(b):
            cnt+=1
            total+=c
            union(a,b)
            if cnt==n-1: return total
    return 0

n,m,k=map(int,input().split())
graph=[]
for _ in range(1,m+1):
    a,b=map(int,input().split())
    graph.append((a,b,_))
graph.sort(key=lambda x: x[2])

answer=[]
for _ in range(k):
    p=[-1]*(n+1)
    result=kruskal(_)
    answer.append(result)
    if not result:
        while len(answer)<k:
            answer.append(0)
        break
print(*answer)
