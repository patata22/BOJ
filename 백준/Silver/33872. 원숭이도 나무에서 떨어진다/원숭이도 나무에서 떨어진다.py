def sol(now,hp,score):
    if hp==0:
        if now==e:
            global answer
            answer=max(answer,score)
        return
    for to in graph[now]:
        if hawk[to] or visited[to]==2: continue
        if not visited[to]:
            visited[to]+=1
            sol(to,hp-1,score+banana[to])
            visited[to]-=1
        else:
            visited[to]+=1
            sol(to,hp-1,score)
            visited[to]-=1

n,h=map(int,input().split())

s,e=map(int,input().split())
s-=1
e-=1

banana=list(map(int,input().split()))
hawk=list(map(int,input().split()))
graph=[[] for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited=[0]*n
visited[s]=1
answer=-1

sol(s,h,banana[s])

print(answer)