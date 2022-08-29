def sol(cnt):
    if cnt==m:
        print(' '.join(map(str,choose)))
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=1
            choose.append(i)
            sol(cnt+1)
            choose.pop()
            visited[i]=0
            
        

n,m=map(int,input().split())
choose=[]
visited=[0]*(n+1)

sol(0)
