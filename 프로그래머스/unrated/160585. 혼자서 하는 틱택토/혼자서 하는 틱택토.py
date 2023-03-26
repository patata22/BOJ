def solution(board):
    board=[list(x) for x in board]
    o,x=0,0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':o+=1
            elif board[i][j]=='X':x+=1
    if o-x not in (0,1): return 0
    
    def checkWin(target):
        for i in range(3):
            if board[i]==[target]*3: return True
        for j in range(3):
            finish=True
            for i in range(3):
                if board[i][j]!=target:
                    finish=False
            if finish: return True
        
        finish=True
        for i in range(3):
            if board[i][i]!=target: finish=False
        if finish: return True
        finish=True
        for i in range(3):
            if board[2-i][i]!=target:finish=False
        if finish: return True
        
        return False

    if checkWin('O') and checkWin('X'): return 0
    if checkWin('O') and o==x: return 0
    if checkWin('X') and o!=x: return 0
    return 1
   
    