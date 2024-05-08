def checkRow(i,j):
    if sum(visited[i])==2: return 1
    return 0

def checkCol(i,j):
    if visited[0][j]+visited[1][j]+visited[2][j]==2: return 1
    return 0

def checkDiag(i,j):
    return checkRight(i,j) + checkLeft(i,j)

def checkRight(i,j):
    if i==j and visited[0][0]+visited[1][1]+visited[2][2]==2: return 1
    return 0

def checkLeft(i,j):
    if i+j==2 and visited[0][2]+visited[1][1]+visited[2][0]==2: return 1
    return 0

def calcScore(i,j):
    return checkRow(i,j)+checkCol(i,j)+checkDiag(i,j)
        
def getScoreLine():
    for i in range(9):
        now=word[i]
        i,j=location[now]
        scoreLine.append(calcScore(i,j))
        visited[i][j]=1
        
def sol(depth):
    global finish
    if finish: return
    if depth==9:
        finish=True
        return
    for i in range(9):
        if not used[i]:
            now=word[i]
            x,y=location[now]
            if calcScore(x,y)==scoreLine[depth]:
                answer.append(now)
                visited[x][y]=1
                used[i]=1
                sol(depth+1)
                if finish: return
                used[i]=0
                visited[x][y]=0
                answer.pop()

for tt in range(int(input())):
    word=list(input())
    board=[list(input()) for i in range(3)]
    location={}
    for i in range(3):
        for j in range(3):
            location[board[i][j]]=(i,j)
    scoreLine=[]
    used=[0]*9
    visited=[[0]*3 for i in range(3)]
    getScoreLine()
    visited=[[0]*3 for i in range(3)]

    finish=False
    answer=[]
    word.sort()
    sol(0)
    print(''.join(map(str,scoreLine)),''.join(answer))
