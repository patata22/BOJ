n,m,k=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
answer=0
turn=float('inf')

for i in range(n):
    temp=0
    for j in range(m):
        temp+=board[i][j]
        if temp>=k:
            if j<turn:
                answer=i
                turn=j
            break

print(answer+1, turn+1)