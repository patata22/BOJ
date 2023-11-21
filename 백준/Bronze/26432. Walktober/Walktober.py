for t in range(1,int(input())+1):
    answer=0
    n,m,p=map(int,input().split())
    p-=1
    board=[tuple(map(int,input().split())) for i in range(n)]
    for i in range(m):
        mine=board[p][i]
        temp=0
        for j in range(n):
            temp=max(temp,board[j][i])
        answer+=temp-mine
    print(f'Case #{t}: {answer}')