from heapq import heappush,heappop
import sys
input=sys.stdin.readline
def fox():
    hp=[[0,1]]  
    while hp:
        t,now=heappop(hp)
        if d_fox[now]!=t:continue
        for v,w in graph[now]:
            nt=t+w
            if d_fox[v]>nt:
                d_fox[v]=nt
                heappush(hp,(nt,v))
def wolf():
    hp=[[0,1,True]]
    while hp:
        t,now,con=heappop(hp)
        if con and d_wolf[0][now]!=t:continue
        elif not con and d_wolf[1][now]!=t:continue
        for v,w in graph[now]:
            if con and d_wolf[1][v]>t+w//2:
                d_wolf[1][v]=t+w//2
                heappush(hp,(t+w//2,v,False))
            elif not con and d_wolf[0][v]>t+w*2:
                d_wolf[0][v]=t+w*2
                heappush(hp,(t+w*2,v,True))
    return d_wolf
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,d=map(int,input().split())
    graph[a].append((b,2*d))
    graph[b].append((a,2*d))
d_wolf=[[float('inf')]*(n+1) for i in range(2)]
d_wolf[0][1]=0
d_fox=[float('inf')]*(n+1)
d_fox[1]=0
fox()
wolf()
answer=0
for i in range(1,n+1):
    if d_fox[i]<min(d_wolf[0][i],d_wolf[1][i]):answer+=1
print(answer)