dx=(-1,1,0,0)
dy=(0,0,-1,1)

def findLeftArm():
    y=sy
    cnt=0
    while y-1>=0 and board[sx][y-1]=='*':
        y-=1
        cnt+=1
    return cnt

def findRightArm():
    y=sy
    cnt=0
    while y+1<n and board[sx][y+1]=='*':
        y+=1
        cnt+=1
    return cnt

def findLeftLeg():
    x=sx
    body=0
    while board[x+1][sy]=='*':
        x+=1
        body+=1
    cnt=0
    while x+1<n and board[x+1][sy-1]=='*':
        cnt+=1
        x+=1
    return body,cnt
    
def findRightLeg():
    x=sx
    while board[x+1][sy]=='*':
        x+=1
    cnt=0
    while x+1<n and board[x+1][sy+1]=='*':
        cnt+=1
        x+=1
    return cnt            

n=int(input())
board=[list(input()) for i in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j]=='*':
            cnt=0
            for k in range(4):
                nx,ny=i+dx[k],j+dy[k]
                if 0<=nx<n and 0<=ny<n and board[nx][ny]=='*':
                    cnt+=1
            if cnt==4:
                sx,sy=i,j
print(sx+1,sy+1)
print(findLeftArm(), findRightArm(), *findLeftLeg(), findRightLeg())
