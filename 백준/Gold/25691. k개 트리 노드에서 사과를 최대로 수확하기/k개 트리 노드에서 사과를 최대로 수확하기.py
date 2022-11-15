def sol(apple, move,visited, now):
    global answer
    if move==k:
        answer=max(answer,apple)
        return
    for to in graph[now]:
        if (visited>>to)%2==1:
            if (apple, visited, to) not in visit:
                visit.add((apple,visited,to))
                sol(apple, move, visited, to)
        else:
            sol(apple+number[to],move+1, (1<<to)|visited, to)
                
        

n,k=map(int,input().split())

graph=[[] for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

number=tuple(map(int,input().split()))
visit = set()

answer=0

if number[0]:
    sol(1,1,1,0)
else: sol(0,1,1,0)

print(answer)
