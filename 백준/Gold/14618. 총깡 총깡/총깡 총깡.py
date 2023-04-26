import sys,heapq
input=sys.stdin.readline

def sol():
    
    q=[]
    q.append((0,j))
    distance[j]=0
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))

n,m=map(int,input().split())
j=int(input())
k=int(input())
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))

graph=[[] for i in range(n+1)]
distance=[float('inf')]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

a=float('inf')
b=float('inf')

sol()
for x in A:
    a=min(distance[x],a)
for x in B:
    b=min(distance[x],b)

if a==float('inf') and b==float('inf'):
    print(-1)
elif a<=b:
    print('A')
    print(a)
elif a>b:
    print('B')
    print(b)
