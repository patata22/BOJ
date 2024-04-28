import heapq

def sol():
    q=[(-value[1],1)]
    answer=0
    
    while q:
        v=-q[0][0]
        now=heapq.heappop(q)[1]
        answer+=v
        print(answer)
        for to in graph[now]:
            heapq.heappush(q,(-value[to],to))
    
n=int(input())
parent=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
for i in range(n-1):
    p = parent[i]
    graph[p].append(i+2)
value=[0]+list(map(int,input().split()))
sol()
