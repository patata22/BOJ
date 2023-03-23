def solution(n,m, queries):
    
    board= [[0]*m for i in range(n)]
    now=0
    for i in range(n):
        for j in range(m):
            now+=1
            board[i][j]=now
    answer = []
    
    def rotate(x1,y1,x2,y2):     
        temp=board[x1][y1]
        minimum=temp
        for j in range(y1+1, y2+1):
            now=board[x1][j]
            board[x1][j]=temp
            temp=now
            minimum=min(minimum, temp)
        for i in range(x1+1, x2+1):
            now=board[i][y2]
            board[i][y2]=temp
            temp=now
            minimum=min(minimum, temp)
        for j in range(y2-1, y1-1,-1):
            now=board[x2][j]
            board[x2][j]=temp
            temp=now
            minimum=min(minimum, temp)
        for i in range(x2-1, x1-1,-1):
            now=board[i][y1]
            board[i][y1]=temp
            temp=now
            minimum=min(minimum, temp)
        return minimum
    
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(x1-1,y1-1,x2-1,y2-1))            
    
    return answer