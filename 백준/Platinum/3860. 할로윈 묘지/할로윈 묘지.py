import sys
input=sys.stdin.readline

dx = (1,0)
dy = (0,1)

def bellman_ford():
    global cycle
    graph = [[[] for i in range(m)] for i in range(n)]
    for x in range(n):
        for y in range(m):
            if (x,y) in tomb: continue
            for d in range(2):
                nx,ny= x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<m:
                    graph[x][y].append((nx,ny))
                    graph[nx][ny].append((x,y))
    graph[-1][-1]=[]
    for a,b in tomb:
        graph[a][b] = []
    for a,b in hole:
        graph[a][b] = []
    distance = [[float('inf')]*m for i in range(n)]
    distance[0][0] = 0
    
    total = n*m - len(tomb)
    for i in range(total):
        for x in range(n):
            for y in range(m):
                if distance[x][y]==float('inf'): continue
                dist = distance[x][y]
                for nx,ny in graph[x][y]:
                    if distance[nx][ny]>dist+1:
                        distance[nx][ny]=dist+1
                        if i==total-1:
                            cycle=True
                            return
        for temp in hole:
            a,b = temp
            if distance[a][b] == float('inf'): continue
            nx,ny,t = hole[temp]
            if distance[nx][ny]> distance[a][b]+t:
                distance[nx][ny] = distance[a][b]+t
                if i==total-1:
                    cycle=True
                    return
    return distance[-1][-1]

while True:
    m,n = map(int,input().split())
    if m==0 and n==0: break
    
    tomb = set()
    for _ in range(int(input())):
        b,a = map(int,input().split())
        tomb.add((a,b))
    hole = {}
    for _ in range(int(input())):
        y1,x1,y2,x2,t = map(int,input().split())
        hole[(x1,y1)] = (x2,y2,t)
    cycle = False
    answer = bellman_ford()
    if cycle: print('Never')
    elif answer == float('inf'): print('Impossible')
    else: print(answer)
