import sys
input=sys.stdin.readline

def calcRow(x):
    global rowSum,rowCnt
    if rowDeleted[x]: return 0
    result=(n*(n+1))//2+n*x
    result-=colSum+colCnt*x
    rowDeleted[x]=1
    rowSum+=x
    rowCnt+=1
    return result

def calcCol(x):
    global colSum,colCnt
    if colDeleted[x]: return 0
    result=(n*(n+1))//2+n*x
    result-=rowSum+rowCnt*x
    colDeleted[x]=1
    colSum+=x
    colCnt+=1
    return result

n,q=map(int,input().split())
rowDeleted=[0]*(n+1)
colDeleted=[0]*(n+1)
rowSum=0
colSum=0
rowCnt=0
colCnt=0


answer=[]
for _ in range(q):
    cmd,x=input().split()
    if cmd=='R': answer.append(calcRow(int(x)))
    else: answer.append(calcCol(int(x)))

print(*answer,sep='\n')
