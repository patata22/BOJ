import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def makeTree(now, parent):
    for to in graph[now]:
        if to != parent:
            child[now].append(to)
            makeTree(to, now)

def countSubTree(now):
    for to in child[now]:
        countSubTree(to)
        answer[now]+=answer[to]
            
n,r,q = map(int,input().split())
graph = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]
answer= [1]*(n+1)
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(r, -1)
countSubTree(r)

for _ in range(q):
    print(answer[int(input())])
