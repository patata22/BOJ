import sys
input=sys.stdin.readline

for _ in range(int(input())):
    l,r,n,m,=map(int,input().split())
    x=abs(n-m)
    if x==0:print('G')
    elif l>=x and r>=x:print('E')
    elif l>=x:print('L')
    else:print('R')