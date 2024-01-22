import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    distance=[float('inf')]*(n+1)
    q.append((0,e))
    distance[e]=0
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]!=dist:continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))

    answer=0
    for i in range(1,n+1):
        if distance[i]<=t: answer+=1
    return answer

n=int(input())
e=int(input())
t=int(input())
graph=[[] for i in range(n+1)]
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    graph[b].append((a,c))

print(sol())
