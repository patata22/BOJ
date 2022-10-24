import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def sol(x):
    if answer[x]==1:
        for y in graph[x]:
            answer[x]=max(answer[x],sol(y)+1)
    return answer[x]

n,m=map(int,input().split())
height= [0]+list(map(int,input().split()))
answer=[1]*(n+1)
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    if height[a]>height[b]: graph[b].append(a)
    elif height[a]<height[b]: graph[a].append(b)

visited=[0]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        visited[i]=1
        sol(i)
for i in range(1,n+1):
    print(answer[i])
