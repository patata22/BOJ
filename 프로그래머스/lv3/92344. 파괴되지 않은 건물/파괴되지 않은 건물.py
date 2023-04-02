def solution(board, skill):
    answer = 0
    
    n=len(board)
    m=len(board[0])
    
    damage=[[0]*(m+1) for i in range(n+1)]
    
    for t,x1,y1,x2,y2,degree in skill:
        if t==1:degree*=-1
        damage[x1][y1]+=degree
        damage[x2+1][y2+1]+=degree
        damage[x1][y2+1]-=degree
        damage[x2+1][y1]-=degree
    
    for i in range(n):
        for j in range(1,m):
            damage[i][j]+=damage[i][j-1]
            
    for i in range(1,n):
        for j in range(m):
            damage[i][j]+=damage[i-1][j]
    
    for i in range(n):
        for j in range(m):
            if board[i][j]+damage[i][j]>0:
                answer+=1
            
    
    return answer