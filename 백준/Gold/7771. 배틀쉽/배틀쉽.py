def useRow(x):
    row[x]=1
    if x-1>=0: row[x-1]=1
    if x+1<10: row[x+1]=1

board=[list(map(int,input().split())) for i in range(10)]
row=[0]*10
answer=[['.']*10 for i in range(10)]

for x in range(10):
    for y in range(10):
        if board[x][y]==100:
            useRow(x)
            answer[x][y]='#'
            cnt=3
            for j in range(y+2,10,2):
                if cnt==0: break
                answer[x][j]='#'
                cnt-=1
            for j in range(y-2,-1,-2):
                if cnt==0: break
                answer[x][j]='#'
                cnt-=1

for x in range(10):
    if not row[x]:
        useRow(x)
        answer[x] = '##.##...##'
        break

for x in range(10):
    if not row[x]:
        useRow(x)
        answer[x]='###....###'
        break

for x in range(10):
    if not row[x]:
        useRow(x)
        answer[x]='####......'
        break

for i in range(10):
    print(''.join(answer[i]))