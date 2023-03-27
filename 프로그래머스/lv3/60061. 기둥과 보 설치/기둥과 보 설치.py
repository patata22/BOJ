def solution(n, build_frame):
    answer = []
    
    #가로축 1-index 사용
    pillar= [[0]*(n+2) for i in range(n+1)]
    board= [[0]*(n+2) for i in range(n+1)]
    
    for y,x,isBoard,build in build_frame:
        y+=1
        if build:
            #보 설치
            if isBoard:
                #밑에 기둥이 있거나 오른쪽 밑에 기둥 있거나 양쪽이 보
                if pillar[x-1][y] or pillar[x-1][y+1] or (board[x][y-1] and board[x][y+1]):
                    board[x][y]=1
            #기둥 설치
            else:
                #바닥이거나, 밑에 기둥이 있거나, 내위치 or 위치-1에 보가 있거나
                if x==0 or pillar[x-1][y] or board[x][y] or board[x][y-1]:
                    pillar[x][y]=1
        else:   
            remove=True
            #보 제거
            if isBoard:
                #위에 기둥 있는 경우
                if pillar[x][y]:
                    #밑에 기둥이 있거나 왼쪽에 보가 있어야함
                    if not (pillar[x-1][y] or board[x][y-1]):
                        remove=False
                #오른쪽에 기둥 있는 경우:
                if pillar[x][y+1]:
                    #오른쪽 밑에 기둥이 있거나 오른쪽에 보가 있어야함
                    if not (pillar[x-1][y+1] or board[x][y+1]):
                        remove=False
                #왼쪽에 보 있는 경우:
                if board[x][y-1]:
                    # 그 보의 아래에 기둥 있어야함
                    if not (pillar[x-1][y-1] or pillar[x-1][y]):
                        remove=False
                #오른쪽에 보 있는 경우
                if board[x][y+1]:
                    # 그 보의 아래에 기둥 있어야함
                    if not (pillar[x-1][y+1] or pillar[x-1][y+2]):
                        remove=False
                if remove: board[x][y]=0
            #기둥 제거
            else:
                #위에 기둥 있는 경우
                if pillar[x+1][y]:
                    # 윗칸 한쪽에 보 있어야함
                    if not (board[x+1][y] or board[x+1][y-1]):
                        remove=False
                #보 있는 경우
                if board[x+1][y]:
                    # 오른쪽에 기둥이 있거나 좌우에 보가 있어야함
                    if not (pillar[x][y+1] or (board[x+1][y-1] and board[x+1][y+1])):
                        remove=False
                #왼쪽에 보 있는 경우
                if board[x+1][y-1]:
                    # 왼쪽에 기둥이 있거나 좌우에 보가 있어야함
                    if not (pillar[x][y-1] or (board[x+1][y-2] and board[x+1][y])):
                        remove=False
                if remove: pillar[x][y]=0
    
    for i in range(n+1):
        for j in range(n+2):
            if board[i][j]:
                answer.append([j-1,i,1])
            if pillar[i][j]:
                answer.append([j-1,i,0]) 
    answer.sort()
    
    return answer