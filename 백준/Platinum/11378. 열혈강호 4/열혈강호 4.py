import sys
input=sys.stdin.readline

def dfs(x):
    if visited[x]:return False
    visited[x]=1
    for t in task[x]:
        if solved[t]==-1 or dfs(solved[t]):
            solved[t]=x
            return True

n,m,k=map(int,input().split())
task=[list(map(int,input().split()))[1:] for i in range(n)]
solved = [-1]*(m+1)
answer=0
for i in range(n):
    visited=[0]*n
    if dfs(i):answer+=1
    
    
for i in range(n):
    while k>0:
        visited=[0]*n
        if dfs(i):
            answer+=1
            k-=1
        else:break
print(answer)
