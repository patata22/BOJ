import sys,heapq
input=sys.stdin.readline

def makeGraph(point1,point2):
    z1,x1,y1=point1
    z2,x2,y2=point2
    z1*=5
    z2*=5
    return ((z2-z1)**2+(x2-x1)**2+(y2-y1)**2)**0.5

def sol(start,end):
    q=[]
    q.append((0,start))
    distance=[float('inf')]*n
    distance[start]=0
    prev=[-1]*n
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        if now==end:
            result=[]
            while now!=-1:
                result.append(now)
                now=prev[now]
            return result[::-1]
        for to,d in graph[now]:
            if distance[to]>dist+d:
                prev[to]=now
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
                
    return -1

n,m=map(int,input().split())
point=[tuple(map(int,input().split())) for i in range(n)]
graph=[[] for i in range(n)]


for _ in range(m):
    a,b,c=input().rstrip().split()
    a,b=int(a),int(b)
    if c=='walking' or c=='stairs':
        dist=makeGraph(point[a],point[b])
        graph[a].append((b,dist))
        graph[b].append((a,dist))
    elif c=='lift':
        graph[a].append((b,1))
        graph[b].append((a,1))
    else:
        dist=makeGraph(point[a],point[b])
        graph[a].append((b,1))
        graph[b].append((a,dist*3))

for _ in range(int(input())):
    print(*sol(*map(int,input().split())))
