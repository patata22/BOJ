def solution(keyinput, board):
    direction={'up':(0,1), 'down':(0,-1),'left':(-1,0), 'right':(1,0)}
    X=board[0]//2
    Y=board[1]//2
    x,y=0,0
    
    for i in keyinput:
        dx,dy=direction[i]
        if -X<=x+dx<=X and -Y<=y+dy<=Y:
            x+=dx
            y+=dy
    return [x,y]