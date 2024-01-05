import sys
input=sys.stdin.readline

n,p=map(int,input().split())
score={}
w,l,g=map(int,input().split())
for i in range(p):
    a,b=input().rstrip().split()
    if b=='W':score[a]=w
    else: score[a]=-l
now=0

answer='I AM IRONMAN!!'
for _ in range(n):
    temp=input().rstrip()
    if temp in score:
        x=score[temp]
        if x>=0:
            now+=w
            if now>=g: answer='I AM NOT IRONMAN!!'
        else: now=max(0,now-l)
    else:
        now=max(0,now-l)
print(answer)
