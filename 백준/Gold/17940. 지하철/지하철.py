import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    q.append((0,0,0)) #환승, 거리, 역
    distance=[[float('inf')]*n for i in range(n)]
    distance[0][0]=0
    while q:
        transfer,dist,now = heapq.heappop(q)
        if distance[now][transfer]!=dist: continue
        if now==m: return transfer,dist
        for j in range(n):
            if graph[now][j]:
                temp=company[now]!=company[j]
                if distance[j][transfer+temp]>dist+graph[now][j]:
                    distance[j][transfer+temp]=dist+graph[now][j]
                    heapq.heappush(q,(transfer+temp,dist+graph[now][j], j))

n,m=map(int,input().split())
company=[int(input()) for i in range(n)]
graph=[tuple(map(int,input().split())) for i in range(n)]

print(*sol())