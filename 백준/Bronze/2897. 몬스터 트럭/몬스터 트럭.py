def check(x,y):
    temp=0
    for i in range(x,x+2):
        for j in range(y,y+2):
            if board[i][j]=='#':return
            elif board[i][j]=='X': temp+=1
    answer[temp]+=1
    
r,c=map(int,input().split())

board = [list(input()) for i in range(r)]

answer=[0]*5

for i in range(r-1):
    for j in range(c-1):
        check(i,j)

for x in answer:print(x)
