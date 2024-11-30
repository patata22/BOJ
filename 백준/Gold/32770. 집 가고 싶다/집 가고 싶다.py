import sys,heapq
input=sys.stdin.readline

def sol(x,y):
    q=[]
    q.append((0,x))
    distance=[float('inf')]*unused
    distance[x]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        if now==y: return dist
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
                

    return float('inf')

n=int(input())
nameToNum = {}
unused=0
graph={}
for _ in range(n):
    a,b,c=input().split()
    if a not in nameToNum:
        nameToNum[a]=unused
        graph[unused]=[]
        unused+=1
    a=nameToNum[a]
    if b not in nameToNum:
        nameToNum[b]=unused
        graph[unused]=[]
        unused+=1
    b=nameToNum[b]
    graph[a].append((b,int(c)))


answer=sol(nameToNum['sasa'],nameToNum['home'])+sol(nameToNum['home'],nameToNum['sasa'])
if answer==float('inf'): print(-1)
else: print(answer)
