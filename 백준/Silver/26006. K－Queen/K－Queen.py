import sys
input=sys.stdin.readline

n,k=map(int,input().split())
r,c=map(int,input().split())
move = [[0]*3 for i in range(3)]
if r==1:
    move[0]=[1]*3
elif r==n: move[2] = [1]*3

if c==1:
    move[0][0]=1
    move[1][0]=1
    move[2][0]=1
elif c==n:
    move[0][2]=1
    move[1][2]=1
    move[2][2]=1
    
for _ in range(k):
    x,y = map(int,input().split())

    #가로
    if x==r-1: move[0]=[1]*3
    elif x==r: move[1]=[1]*3
    elif x==r+1: move[2] = [1]*3
    #세로
    if y==c-1:
        for i in range(3):
            move[i][0]=1
    elif y==c:
        for i in range(3):
            move[i][1]=1
    elif y==c+1:
        for i in range(3):
            move[i][2]=1
    #우하 - 1,n으로부터의 거리
    d = x-1 + n- y
    k = r-1 + n-c
    if d-k==-2: move[0][2]=1
    elif d-k==-1:
        move[0][1]=1
        move[1][2]=1
    elif d-k==0:
        move[0][0]=1
        move[1][1]=1
        move[2][2]=1
    elif d-k==1:
        move[1][0]=1
        move[2][1]=1
    elif d-k==2:
        move[2][0]=1
        
    #좌하 - 원점에 대한 합으로 쓴다
    if x+y == r+c-2:
        move[0][0]=1
    elif x+y == r+c-1:
        move[0][1]=1
        move[1][0]=1
    elif x+y == r+c:
        move[0][2]=1
        move[1][1]=1
        move[2][0]=1
    elif x+y==r+c+1:
        move[1][2]=1
        move[2][1]=1
    elif x+y==r+c+2:
        move[2][2]=1

onAttack = move[1][1]
moveable= 0
for i in range(3):
    for j in range(3):
        if i==j==1: continue
        if not move[i][j]: moveable = 1

if onAttack and not moveable: print('CHECKMATE')
elif onAttack and moveable: print('CHECK')
elif not onAttack and not moveable: print("STALEMATE")
else: print('NONE')