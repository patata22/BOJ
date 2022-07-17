import sys
input=sys.stdin.readline

def find(a):
    if p[a]==a:return a
    else: return find(p[a])

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:p[b]=a
    
def kruskal():
    cnt=0
    cost=0
    for x in graph:
        a,b,c=x
        if find(a)!=find(b):
            cnt+=1
            cost+=c
            union(a,b)
            if cnt==n-1: return cost

n=int(input())

p=[i for i in range(n+1)]
graph=[tuple(map(int,input().split())) for i in range(int(input()))]
graph.sort(key=lambda x: (x[2],x[0],x[1]))

print(kruskal())
