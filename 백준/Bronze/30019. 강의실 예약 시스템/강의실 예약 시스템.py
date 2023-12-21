import sys
input=sys.stdin.readline

n,m=map(int,input().split())
room=[0]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    if b>=room[a]:
        print('YES')
        room[a]=c
    else:print('NO')
