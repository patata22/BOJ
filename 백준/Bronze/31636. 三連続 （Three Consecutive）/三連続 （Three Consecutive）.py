n=int(input())
board=list(input())
answer='No'
for i in range(n-2):
    if board[i]=='o' and board[i+1]=='o' and board[i+2]=='o':answer='Yes'
print(answer)