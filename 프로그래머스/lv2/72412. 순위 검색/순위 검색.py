def solution(info, query):
    for i in info: processInfo(i)
    prefix()
    return [answerQuery(q) for q in query]
    return answer

def processInfo(info):
    l,p,c,f,score = info.split(' ')
    score=int(score)
    for i in (0, language[l]):
        for j in (0, position[p]):
            for k in (0,career[c]):
                for h in (0, food[f]):
                    board[i][j][k][h][score]+=1
                    
def answerQuery(q):
    l,p,c,f,score=q.replace('and','').split()
    score=int(score)
    l=language[l]
    p=position[p]
    c=career[c]
    f=food[f]
    return board[l][p][c][f][score]

def prefix():
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(99999,-1,-1):
                        
                        board[i][j][k][l][m]+=board[i][j][k][l][m+1]

language={'-':0, 'cpp':1, 'java':2, 'python':3}
position={'-':0, 'backend': 1, 'frontend': 2}
career={'-':0, 'junior':1, 'senior':2}
food={'-':0, 'chicken':1, 'pizza':2}
 
board=[[[[[0]*100001 for i in range(3)] for i in range(3)] for i in range(3)] for i in range(4)]