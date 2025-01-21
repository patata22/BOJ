import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(now,cost):
   visited[now]=1
   solved=0
   time=0
   node=now
   for to,c in graph[now]:
      if not visited[to]:
         s,t,nd=sol(to,c)
         if s>solved:
            solved=s
            time=t
            node=nd
         elif s==solved:
            if t<time:
               time=t
               node=nd

   return solved+1,time+cost,node

n,T=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
   a,b,c=map(int,input().split())
   graph[a].append((b,c))
   graph[b].append((a,c))

visited=[0]*(n+1)
start=sol(1,0)[2]
visited=[0]*(n+1)
solved,time,node=sol(start,0)
answer= time//T
if time%T: answer+=1

print(answer)
