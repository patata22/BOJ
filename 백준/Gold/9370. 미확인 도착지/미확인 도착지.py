import sys,heapq
input=sys.stdin.readline

MAX=10**8

def sol():
    q=[(0,s)]
    distance=[MAX]*(n+1)
    distance[s]=0
    while q:
        cost,now=heapq.heappop(q)
        if cost!=distance[now]:continue
        for to,c in graph[now]:
            if distance[to]>cost+c:
                distance[to]=cost+c
                heapq.heappush(q,(cost+c,to))
    return distance

for T in range(int(input())):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        if (a,b)==(g,h) or (a,b)==(h,g):
            c-=0.5
        graph[a].append((b,c))
        graph[b].append((a,c))
    target=[int(input()) for i in range(t)]

    distance=sol()

    answer=[]
    for x in target:
        if type(distance[x])==float:
            answer.append(x)
    answer.sort()
    print(*answer)
