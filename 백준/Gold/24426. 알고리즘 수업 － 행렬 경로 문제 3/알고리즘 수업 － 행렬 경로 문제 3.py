dx=(-1,0)
dy=(0,-1)

def sol1():
    for x in range(mx+1):
        for y in range(my+1):
            temp=0
            for i in range(2):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    temp=max(board1[nx][ny],temp)
            board1[x][y]+=temp
    for x in range(mx,n):
        for y in range(my,n):
            temp=0
            for i in range(2):
                nx,ny=x+dx[i],y+dy[i]
                if mx<=nx<n and my<=ny<n:
                    temp=max(board1[nx][ny],temp)
            board1[x][y]+=temp
    return board1[-1][-1]

def sol2():
    for x in range(n):
        for y in range(n):
            add=False
            temp=-float('inf')
            for i in range(2):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    add=True
                    temp=max(board2[nx][ny],temp)
            if add:board2[x][y]+=temp
    return board2[-1][-1]
    
    
n=int(input())

board1=[]
board2=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    board1.append(temp)
    board2.append(temp[:])

mx,my=map(lambda x: int(x)-1,input().split())
board2[mx][my]=-float('inf')
print(sol1(),sol2())
