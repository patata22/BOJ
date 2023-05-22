import sys
input=sys.stdin.readline

n,q=map(int,input().split())
score=[0]+list(map(int,input().split()))
square=[0]*(n+1)
for i in range(1,n+1):
    square[i]=square[i-1]+score[i]**2
    score[i]+=score[i-1]
for _ in range(q):
    a,b=map(int,input().split())
    a-=1
    print(((score[b]-score[a])**2-(square[b]-square[a]))//2)