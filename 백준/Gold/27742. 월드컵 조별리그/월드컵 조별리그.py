import sys
input=sys.stdin.readline

def sol():
    l=-1
    r=10**12+1
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else: l=mid
    if r<=k: return r
    else:return -1

def check(mid):
    temp=score[:]
    ee = earn[:]
    aa = allow[:]
    ee[X]+=mid
    aa[Y]+=mid
    if mid>board[Y][X]: temp[X]+=3
    elif mid==board[Y][X]:
        temp[X]+=1
        temp[Y]+=1
    else: temp[Y]+=3
    temp=list(enumerate(temp))
    temp.sort(key=lambda x: (-x[1], -(ee[x[0]]-aa[x[0]]),-ee[x[0]],x[0]))
    for i in range(2):
        if temp[i][0]==X: return True
    return False

T,k=map(int,input().split())
T-=1

board=[list(map(int,input().split())) for i in range(4)]
score=[0]*4
earn=[0]*4
allow=[0]*4

for i in range(4):
    for j in range(4):
        if board[i][j]==-1: X,Y=i,j

for i in range(4):
    for j in range(i+1,4):
        e=board[i][j]
        a=board[j][i]
        if e!=-1:
            earn[i]+=e
            allow[j]+=e
        if a!=-1:
            earn[j]+=a
            allow[i]+=a
        if e!=-1 and a!=-1:
            if board[i][j]>board[j][i]: score[i]+=3
            elif board[i][j]==board[j][i]:
                score[i]+=1
                score[j]+=1
            else: score[j]+=3

print(sol())
