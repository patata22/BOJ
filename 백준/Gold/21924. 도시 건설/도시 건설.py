import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    pa,pb=find(a),find(b)
    if pa!=pb:
        p[b]=pa

def kruskal():
    cost=0
    count=0
    for a,b,c in graph:
        a,b=find(a),find(b)
        if a!=b:
            union(a,b)
            count+=1
            cost+=c
            if count==n-1: return cost
    return -1

n,m=map(int,input().split())
graph=[tuple(map(int,input().split())) for i in range(m)]
graph.sort(key=lambda x: x[2])
total=sum([x[2] for x in graph])
p=[-1]*(n+1)
k=kruskal()
if k==-1:print(-1)
else:print(total-k)
