def solution(n, s, a, b, fares):
    
    
    distance=[[float('inf')]*(n+1) for i in range(n+1)]
    for i in range(1,n+1): distance[i][i]=0
    for start, end , cost in fares:
        distance[start][end]=cost
        distance[end][start]=cost
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if distance[i][j]>distance[i][k]+distance[k][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]
    answer = distance[s][a]+distance[s][b]
    
    for i in range(1,n+1):
        answer=min(answer, distance[s][i]+distance[i][a]+distance[i][b])
                
    
    return answer