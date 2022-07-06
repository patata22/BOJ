import sys
input=sys.stdin.readline

def find(a):
    if parent[a]==-1:return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa!=pb: parent[b]=pa

def kruskal():
    answer=0
    cnt=0
    for i in range(e):
        start,end,cost=graph[i]
        a,b=find(start),find(end)        
        if a!=b:
            cnt+=1
            answer+=cost
            union(a,b)
            if cnt==v-1:break
    return answer

v,e = map(int,input().split())
parent=[-1]*(v+1)
graph=[tuple(map(int,input().split())) for i in range(e)]
graph.sort(key = lambda x: x[2])
print(kruskal())
