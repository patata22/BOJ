import sys
input=sys.stdin.readline

MAX=19

m=int(input())

table= [[0]*20 for i in range(m+1)]

temp=tuple(map(int,input().split()))
for i in range(1,m+1):
    table[i][0]=temp[i-1]

for j in range(1,20):
    for i in range(1,m+1):
        table[i][j] = table[table[i][j-1]][j-1]

for _ in range(int(input())):
    n,x=map(int,input().split())
    for i in range(20):
        if n&(1<<i): x = table[x][i]
    print(x)
    