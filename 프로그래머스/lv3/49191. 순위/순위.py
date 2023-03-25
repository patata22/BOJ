from collections import deque

def solution(n, results):
    answer=0
    board=[[float('inf')]*(n+1) for i in range(n+1)]
    for winner, loser in results:
        board[winner][loser]=1
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if board[i][j]>board[i][k]+board[k][j]:
                    board[i][j]=board[i][k]+board[k][j]
                    
    for i in range(1,n+1):
        temp=0
        for j in range(1,n+1):
            if board[i][j]!=float('inf'):temp+=1
            if board[j][i]!=float('inf'):temp+=1
        if temp==n-1: answer+=1
            
        
    return answer