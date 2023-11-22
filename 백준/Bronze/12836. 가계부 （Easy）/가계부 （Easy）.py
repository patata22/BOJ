import sys
input=sys.stdin.readline

n,q=map(int,input().split())
answer=[0]*(n+1)
for _ in range(q):
    c,a,b=map(int,input().split())
    if c==1: answer[a]+=b
    else:
        total=0
        for i in range(a,b+1):
            total+=answer[i]
        print(total)
