import sys
input=sys.stdin.readline

def dfs(x):
    if visited[x]:return False
    visited[x]=1
    for y in cow[x]:
        if house[y]==0 or dfs(house[y]):
            house[y]=x
            return True
    return False

n,m=map(int,input().split())
cow=[[] for i in range(n+1)]
answer=0
for i in range(1,n+1):
    temp=list(map(int,input().split()))
    for j in temp[1:]:cow[i].append(j)
house=[0]*(m+1)

for i in range(1,n+1):
    visited=[0]*(n+1)
    if dfs(i): answer+=1

print(answer)