from collections import deque

def sol(now, move, apple, pair, visit):
    global maxAnswer, maxApple, maxPair
    if move==k:
        if apple*pair>maxAnswer:
            maxAnswer=apple*pair
            maxApple, maxPair = apple, pair
        elif apple*pair==maxAnswer and apple>maxApple:
            maxApple, maxPair = apple, pair
        elif apple*pair==maxAnswer and pair>maxPair:
            maxApple, maxPair = apple, pair
        return

    for to in graph[now]:
        nxt_visit = visit|1<<to
        if not visited[to][nxt_visit]:
            visited[to][nxt_visit]=1
            if (visit>>to)%2:
                sol(to, move, apple,pair,nxt_visit)
            else:
                if fruit[to]==0:
                    sol(to,move+1, apple, pair, nxt_visit)
                elif fruit[to]==1:
                    sol(to,move+1, apple+1, pair, nxt_visit)
                elif fruit[to]==2:
                    sol(to,move+1, apple,pair+1, nxt_visit)
        


n,k=map(int,input().split())
graph=[[] for i in range(n)]
visited=[[0]*(2**18) for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

fruit=tuple(map(int,input().split()))

maxAnswer=0
maxApple, maxPair = 0,0

if fruit[0]==0:
    sol(0,1,0,0,1)
elif fruit[0]==1:
    sol(0,1,1,0,1)
elif fruit[0]==2:
    sol(0,1,0,1,1)

print(maxApple, maxPair)

