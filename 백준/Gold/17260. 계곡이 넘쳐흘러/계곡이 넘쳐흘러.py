import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def sol(now):
   global answer
   visited[now]=1
   h=height[now]
   for to in graph[now]:
      if not visited[to]:
         h=max(h,height[now]+(sol(to)-height[now])//2)
   return h
      

n,k=map(int,input().split())
height=[0]+list(map(int,input().split()))
graph=[[] for i in range(n+1)]

for _ in range(n-1):
   a,b=map(int,input().split())
   graph[a].append(b)
   graph[b].append(a)

visited=[0]*(n+1)
visited[k]=1

result=0
for to in graph[k]:
   result=max(result,sol(to))

print(int(result>=height[k]))

