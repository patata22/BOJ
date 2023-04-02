n=int(input())

answer=[]
difference=float('inf')
boards=[]
def compare(board1, board2):
    temp=0
    for i in range(5):
        for j in range(7):
            if board1[i][j]!=board2[i][j]:
                temp+=1
    return temp


for _ in range(n):
    board=[list(input()) for i in range(5)]
    boards.append(board)

for i in range(n):
    for j in range(i+1,n):
        gap=compare(boards[i],boards[j])
        if gap<difference:
            difference=gap
            answer=[i+1,j+1]
print(*answer)

