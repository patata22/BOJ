def solution(board):
    quad(board,0,0,len(board))
    return answer

def quad(board,x,y,size):
    global answer
    start=board[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if board[i][j]!=start:
                temp=size//2
                quad(board, x,y,temp)
                quad(board, x+temp,y,temp)
                quad(board,x,y+temp,temp)
                quad(board, x+temp, y+temp, temp)
                return
    answer[board[x][y]]+=1

answer=[0,0]