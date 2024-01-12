import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

k=int(input())
number=list(map(int,input().split()))
destroyed=[0]*(n+1)
for i in number:
    destroyed[i]=1
count=[0]*(n+1)
answer=[]
for now in number:
    flag=True
    for to in graph[now]:
        if not destroyed[to]:
            flag=False
            break
    if flag:
        count[now]=1
        for to in graph[now]:
            count[to]=1
        answer.append(now)

if sum(count)==k:
    print(len(answer))
    print(*answer)
else:print(-1)

        
            
