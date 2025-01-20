m,n=map(int,input().split())
original = list(input())

oriCnt = {}
strCnt = {}
for i in range(65,91):
    oriCnt[chr(i)]=0
    strCnt[chr(i)]=0
for i in range(97,123):
    oriCnt[chr(i)]=0
    strCnt[chr(i)]=0
for x in original:
    oriCnt[x]+=1

answer=0

String = list(input())            
matchCnt=0

for i in range(m):
    strCnt[String[i]]+=1

for x in oriCnt:
    if oriCnt[x]==strCnt[x]: matchCnt+=1

if matchCnt==52: answer+=1

l,r=0,m-1
while r+1<n:
    r+=1
    x=String[r]
    beforeCnt=strCnt[x]
    strCnt[x]+=1
    if beforeCnt==oriCnt[x]:
        matchCnt-=1
    elif strCnt[x]==oriCnt[x]:
        matchCnt+=1

    x=String[l]
    beforeCnt=strCnt[x]
    strCnt[x]-=1
    if beforeCnt==oriCnt[x]:
        matchCnt-=1
    elif strCnt[x]==oriCnt[x]:
        matchCnt+=1
    l+=1
    if matchCnt==52: answer+=1

print(answer)
