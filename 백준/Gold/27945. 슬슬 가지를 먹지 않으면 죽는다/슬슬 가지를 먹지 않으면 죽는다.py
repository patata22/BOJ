import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:p[b]=a

def sol():
    now=1
    for a,b,c in graph:
        if c==now and find(a)!=find(b):
            union(a,b)
            now+=1
        else: break
    return now
    
n,m=map(int,input().split())
p=[-1]*(n+1)
graph=[tuple(map(int,input().split())) for i in range(m)]
graph.sort(key=lambda x: x[2])

print(sol())