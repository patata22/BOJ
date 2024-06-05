def sol(depth):
    global finished
    if finished:return
    if depth==5:
        finished=True
        for i in range(9):
            print(*board[i],sep='')
        return
    x,y=zero[depth]
    for i in range(1,10):
        if row[x][i] or col[y][i]: continue
        row[x][i]=1
        col[y][i]=1
        board[x][y]=i
        sol(depth+1)
        board[x][y]=0
        col[y][i]=0
        row[x][i]=0

n=9
for tt in range(int(input())):
    if tt:print()
    board=[list(map(int,input())) for i in range(9)]
    col=[[0]*10 for i in range(9)]
    row=[[0]*10 for i in range(9)]
    zero=[]
    error = False
    for i in range(9):
        for j in range(9):
            if board[i][j]==0: zero.append((i,j))
            else:
                row[i][board[i][j]]+=1
                if row[i][board[i][j]]==2: error=True
                col[j][board[i][j]]+=1
                if col[j][board[i][j]]==2: error=True
                
    for x in range(0,9,3):
        for y in range(0,9,3):
            count=[0]*10
            for i in range(3):
                for j in range(3):
                    count[board[x+i][y+j]]+=1
            for i in range(1,10):
                if count[i]>1: error=True
            
                
                        
        
    finished=False
    if error: print('Could not complete this grid.')
    else:
        sol(0)
        if not finished:print('Could not complete this grid.')
        
