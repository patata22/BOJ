import sys
sys.setrecursionlimit(10000000)
def dfs(i):
    global total
    visited[i]=1
    chain.append(i)
    n=choice[i]
    if visited[n]==1:
        if n in chain:total+=len(chain)-chain.index(n)
        
    else:
        dfs(n)


for _ in range(int(input())):
    n=int(input())
    choice=[0] + list(map(int,input().split()))
    visited=[0 for i in range(n+1)]
    total=0

    for i in range(1,n+1):
        if visited[i]==0:
            chain=[]
            dfs(i)
    print(n-total)
