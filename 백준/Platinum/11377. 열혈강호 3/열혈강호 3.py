import sys
input=sys.stdin.readline

def dfs(x):
    if visited[x]: return False
    visited[x]=1
    for t in task[x][1:]:
        if solved[t]==-1 or dfs(solved[t]):
            solved[t]=x
            return True
def dfs2(x):
    if visited[x]: return False
    visited[x]=1
    for t in task2[x][1:]:
        if solved[t]==-1 or dfs(solved[t]):
            solved[t]=x
            return True
    

n,m,k=map(int,input().split())
task=[]
task2=[]
for i in range(n):
    temp=list(map(int,input().split()))
    task.append(temp)
    task2.append(temp)
solved= [-1]*(m+1)
answer=0
for i in range(n):
    visited=[0]*(n)
    if dfs(i):answer+=1
count=0
for i in range(n):
    visited=[0]*(n)
    if dfs2(i):
        answer+=1
        count+=1
    if count==k: break
print(answer)
