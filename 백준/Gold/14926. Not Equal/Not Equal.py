import sys
sys.setrecursionlimit(10**6)

def sol(now):
    answer.append('a'+str(now))
    for i in range(1,n+1):
        if not visited[now][i]:
            visited[now][i]=1
            visited[i][now]=1
            sol(i)

n=int(input())
visited=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1): visited[i][i]=1
visited[1][n]=visited[n][1]=1
total=(n*(n-1)//2)


answer=[]
sol(1)
answer.append('a1')
print(*answer)
