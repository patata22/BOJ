
for tt in range(1,int(input())+1):
    n,p,m=map(int,input().split())
    friend=[tuple(map(int,input().split())) for i in range(p)]
    distance=[[float('inf')]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        distance[i][i]=0

    for _ in range(m):
        road=list(map(int,input().split()))
        d=road[0]
        for i in range(2,len(road)-1):
            distance[road[i]][road[i+1]]=d
            distance[road[i+1]][road[i]]=d

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if distance[i][j]>distance[i][k]+distance[k][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]

    
    dist=[0]*(n+1)
    dist[0]=float('inf')
    for start,mul in friend:
        for i in range(1,n+1):
            dist[i]=max(dist[i],distance[start][i]*mul)

    answer=min(dist)


    print(f'Case #{tt}: {-1 if answer==float("inf") else answer}')
