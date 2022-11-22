import sys
input=sys.stdin.readline

def bellman_ford(x):
    global cycle
    distance= [float('inf')]*(n+1)
    distance[x] = 0
    for i in range(n):
        for j in range(1,n+1):
            if distance[j]==float('inf'): continue
            for to,d in graph[j]:
                visited[to] = 1
                if distance[to]>distance[j]+d:
                    distance[to] = distance[j]+d
                    if i==n-1:
                        cycle=True
                        return
                    

for t in range(int(input())):
    n,m,w=map(int,input().split())
    graph = [[] for i in range(n+1)]
    visited= [0]*(n+1)
    cycle = False
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    for _ in range(w):
        a,b,c = map(int,input().split())
        graph[a].append((b,-c))

    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=1
            bellman_ford(i)
        if cycle: break
    print('YES') if cycle else print('NO')
