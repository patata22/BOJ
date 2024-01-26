def sol():
    for i in range(n):
        if row[i]==1:
            temp=[]
            for j in range(m):
                if col[j]!=2 and col[j]!=0:
                    temp.append(j)
            a,b=temp
            if col[a]>col[b]:return 'RIGHT'
            else: return 'LEFT'
    for i in range(m):
        if col[i]==1:
            temp=[]
            for j in range(n):
                if row[j]!=2 and row[j]!=0:
                    temp.append(j)
            a,b=temp
            if row[a]>row[b]: return 'DOWN'
            else: return 'UP'

n,m=map(int,input().split())

board=[list(input()) for i in range(n)]
row=[0]*n
col=[0]*m

for i in range(n):
    for j in range(m):
        if board[i][j]=='#':
            row[i]+=1
            col[j]+=1

print(sol())
