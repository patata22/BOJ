import sys
input=sys.stdin.readline

n,q=map(int,input().split())
count=[0]*(n+1)
answer=0
for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        answer+=1-count[a[1]]
        count[a[1]]=1
    elif a[0]==2:
        answer-=count[a[1]]
        count[a[1]]=0
    else:print(n-answer)
