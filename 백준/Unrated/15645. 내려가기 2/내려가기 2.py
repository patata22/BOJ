import sys
input=sys.stdin.readline

n=int(input())
board=[tuple(map(int,input().split())) for i in range(n)]
dp_max=[[0]*3 for i in range(n)]
dp_min=[[0]*3 for i in range(n)]
dp_max[0]=board[0]
dp_min[0]=board[0]

for i in range(1,n):
    dp_max[i][0]=max(dp_max[i-1][0],dp_max[i-1][1])+board[i][0]
    dp_max[i][1]=max(dp_max[i-1])+board[i][1]
    dp_max[i][2]=max(dp_max[i-1][1],dp_max[i-1][2])+board[i][2]
    dp_min[i][0]=min(dp_min[i-1][0],dp_min[i-1][1])+board[i][0]
    dp_min[i][1]=min(dp_min[i-1])+board[i][1]
    dp_min[i][2]=min(dp_min[i-1][1],dp_min[i-1][2])+board[i][2]

print(max(dp_max[-1]), min(dp_min[-1]))