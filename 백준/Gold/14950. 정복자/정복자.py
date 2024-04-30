import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:p[b]=a

def kruskal():
    cnt=0
    answer=0
    ad=0
    for a,b,c in graph:
        if find(a)!=find(b):
            answer+=c+ad
            ad+=t
            union(a,b)
            cnt+=1
            if cnt==n-1: break
    return answer

n,m,t=map(int,input().split())
graph=[tuple(map(int,input().split())) for i in range(m)]
graph.sort(key=lambda x: x[2])
p=[-1]*(n+1)

print(kruskal())
