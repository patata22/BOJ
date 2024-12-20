import sys,heapq
input=sys.stdin.readline

def calcDist(x,y):
    result=0
    for i in range(len(x)):
        result+=(ord(x[i])-ord(y[i]))**2
    return result

def sol():
    q=[]
    q.append((0,s))
    distance=[float('inf')]*n
    distance[s]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        if now==e: return dist
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
                

n=int(input())
graph=[[] for i in range(n)]
temp=[input() for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        dist=calcDist(temp[i],temp[j])
        graph[i].append((j,dist))
        graph[j].append((i,dist))

s,e=map(int,input().split())
s-=1
e-=1

print(sol())
