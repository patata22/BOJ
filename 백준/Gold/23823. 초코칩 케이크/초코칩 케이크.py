import sys
input=sys.stdin.readline

n,q=map(int,input().split())
row=[0]*(n+1)
maxr=0
rowCnt=n
col=[0]*(n+1)
maxc=0
colCnt=n
answer=[]
for _ in range(q):
    a,b=map(int,input().split())
    if a==1:
        row[b]+=1
        if row[b]==maxr: rowCnt+=1
        elif row[b]>maxr:
            maxr=row[b]
            rowCnt=1
    else:
        col[b]+=1
        if col[b]==maxc: colCnt+=1
        elif col[b]>maxc:
            maxc=col[b]
            colCnt=1
    answer.append(str(rowCnt*colCnt))
print('\n'.join(answer))
