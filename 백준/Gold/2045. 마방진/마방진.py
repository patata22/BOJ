board=[list(map(int,input().split())) for i in range(3)]

def sol():
    if board[0][0]==board[1][1]==board[2][2]==0:
        A=board[0][1]+board[0][2]
        B=board[1][0]+board[1][2]
        C=board[2][0]+board[2][1]
        temp=(A+B+C)//2
        board[0][0]=temp-A
        board[1][1]=temp-B
        board[2][2]=temp-C 
        for i in range(3):
            print(*board[i])
            
    elif board[0][2]==board[1][1]==board[2][0]==0:
        A=board[0][0]+board[0][1]
        B=board[1][0]+board[1][2]
        C=board[2][1]+board[2][2]
        temp=(A+B+C)//2
        board[0][2]=temp-A
        board[1][1]=temp-B
        board[2][0]=temp-C
        for i in range(3):
            print(*board[i])
    else:
        total=-1
        zeroCnt=0
        for i in range(3):
            for j in range(3):
                if not board[i][j]: zeroCnt+=1
        for i in range(3):
            total=max(total,sum(board[i]))
        for j in range(3):
            temp=0
            for i in range(3):
                temp+=board[i][j]
            total=max(total,temp)
        total=max(total,board[0][0]+board[1][1]+board[2][2],board[2][0]+board[1][1]+board[0][2])
        while zeroCnt:
            for i in range(3):
                cnt=0
                idx=-1
                for j in range(3):
                    if board[i][j]==0:
                        cnt+=1
                        idx=j
                if cnt==1:
                    zeroCnt-=1
                    board[i][idx]=total-sum(board[i])
            for j in range(3):
                cnt=0
                idx=-1
                temp=0
                for i in range(3):
                    if board[i][j]==0:
                        cnt+=1
                        idx=i
                    temp+=board[i][j]
                if cnt==1:
                    zeroCnt-=1
                    board[idx][j]=total-temp
            
            cnt=0
            idx=-1
            temp=0
            for i in range(3):
                if board[i][i]==0:
                    cnt+=1
                    idx=i
                temp+=board[i][i]
            if cnt==1:
                zeroCnt-=1
                board[idx][idx]=total-temp

            cnt=0
            idx=-1
            temp=0
            for i in range(3):
                if board[2-i][i]==0:
                    cnt+=1
                    idx=i
                temp+=board[i][i]
            if cnt==1:
                zeroCnt-=1
                board[2-idx][idx]=total-temp

        for i in range(3):
            print(*board[i])
            
sol()
