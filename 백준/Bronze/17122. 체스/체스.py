board=[[0]*8 for i in range(8)]
board[0]=[1,0]*4
for i in range(1,8):
    for j in range(8):
        board[i][j]=1-board[i-1][j]
record={}
color=1
for i in range(8):
    for j in range(8):
        record[8*i+j]=board[i][j]
        color=1-color

for _ in range(int(input())):
    a,b=input().split()
    a=board[ord(a[0])-65][int(a[1])-1]
    b=record[int(b)-1]
    print('YES') if a==b else print('NO')
    
