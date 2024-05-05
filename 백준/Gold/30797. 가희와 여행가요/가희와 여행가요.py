import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5*2)

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        p[b]=a

def kruskal():
    cnt=0
    cost=0
    time=0
    for a,b,c,t in graph:
        if find(a)!=find(b):
            cnt+=1
            cost+=c
            time=max(time,t)
            union(a,b)
            if cnt==n-1: return (time,cost)
    return [-1]
    


n,Q=map(int,input().split())
p=[-1]*(n+1)
graph=[tuple(map(int,input().split())) for i in range(Q)]
graph.sort(key=lambda x: (x[2],x[3]))
   
    
print(*kruskal())
