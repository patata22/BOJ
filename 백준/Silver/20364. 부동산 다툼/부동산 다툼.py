import sys
input=sys.stdin.readline

n,q=map(int,input().split())

visited=[0]*(n+1)

for _ in range(q):
    x=int(input())
    temp=x
    pre=0
    while temp:
        if visited[temp]:
            pre=temp
        temp//=2
    if not pre: visited[x]=1
    print(pre)