dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def solved_check(x,y):
    z=int(board[x][y])
    cnt1=0
    cnt2=0
    temp=[]
    changed=False
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny]=='*':
                cnt1+=1
            elif board[nx][ny]=='#':
                temp.append((nx,ny))
                cnt2+=1
        if cnt1==z:
            if temp:changed=True
            for nx, ny in temp:
                board[nx][ny]='.'
            
        elif cnt1+cnt2==z:
            if temp: changed=True
            for nx,ny in temp:
                    board[nx][ny]='*'
    
    return changed

def show():
    for i in range(5):
        print(*board[i])
        

n=int(input())
board=[list(input()) for i in range(n)]

while True:
    changed=False
    for i in range(n):
        if solved_check(0,i):
            changed=True
            solved_check(0,i)
        if solved_check(i,0):
            changed=True
            solved_check(i,0)
        if solved_check(n-1,i):
            changed=True
            solved_check(n-1,i)
        if solved_check(i,n-1):
            changed=True
            solved_check(i,n-1)
    if not changed: break

answer=0
for i in range(n):
    for j in range(n):
        if board[i][j] in ('#', '*'):answer+=1
print(answer)
