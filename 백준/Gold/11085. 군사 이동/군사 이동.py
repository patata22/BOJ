import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a), find(b)
    if a!=b:p[b]=a
        
n,m=map(int,input().split())
C,V=map(int,input().split())

graph=[tuple(map(int,input().split())) for i in range(m)]
graph.sort(key=lambda x: -x[2])
p=[-1]*1001

for x,y,width in graph:
    union(x,y)
    if find(C)==find(V):
        print(width)
        break
