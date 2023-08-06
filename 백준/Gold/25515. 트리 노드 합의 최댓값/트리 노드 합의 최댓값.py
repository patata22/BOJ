import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
    
def sol(now):
    total=value[now]
    for to in graph[now]:
        total+=sol(to)
    if now==0: return total
    return max(total,0)


n=int(input())
graph=[[] for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
value=list(map(int,input().split()))
print(sol(0))

