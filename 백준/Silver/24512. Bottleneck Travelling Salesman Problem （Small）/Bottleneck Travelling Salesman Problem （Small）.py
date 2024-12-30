def sol(depth,now,cost):
    
    global answer,record
    if depth==n-1:
        for to,c in graph[now]:
            if to==temp[0] and answer>max(cost,c):
                answer=max(cost,c)
                record=temp[:]
        return
    for to,c in graph[now]:
        if not visited[to]:
            visited[to]=1
            temp.append(to)
            sol(depth+1,to,max(cost,c))
            temp.pop()
            visited[to]=0
            
    
        
            
n,m=map(int,input().split())
answer=float('inf')
visited=[0]*(n+1)
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
temp=[]
record=[]


for i in range(1,n+1):
    visited[i]=1
    temp.append(i)
    sol(0,i,0)
    temp.pop()
    visited[i]=0

if answer==float('inf'):print(-1)
else:
    print(answer)
    print(*record)
