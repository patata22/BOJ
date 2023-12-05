board=[['.']*20 for i in range(10)]
for _ in range(int(input())):
    temp=input()
    a=ord(temp[0])-65
    b=int(temp[1:])-1
    board[a][b]='o'
for i in range(10):
    print(*board[i], sep='')
