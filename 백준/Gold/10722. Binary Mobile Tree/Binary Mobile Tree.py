import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(x):
    length,leftweight,rightweight=board[x]
    
    if leftweight<0:
        lidx = -leftweight-1
        lweight,lleft,lright=sol(lidx)
        board[x][1]=lweight
    else:
        lleft,lright=0,0
        
    if rightweight<0:
        ridx= -rightweight-1
        rweight,rleft,rright=sol(ridx)
        board[x][2]=rweight
    else:
        rleft,rright=0,0
        
    pivot=(board[x][2]/(board[x][1]+board[x][2]))*length
    left=min(lleft-pivot, rleft+(length-pivot))
    right=max(lright-pivot, rright+(length-pivot))
    
    return board[x][1]+board[x][2],left,right

for tt in range(int(input())):
    n=int(input())
    board=[list(map(int,input().split())) for i in range(n)]
    result=sol(0)
    print(result[2]-result[1])