dx=(1,1,1,0,0,0,-1,-1,-1)
dy=(-1,0,1,-1,0,1,-1,0,1)

def nextMove(a,b):
    if a==x:
        if b<y: return (a,b+1)
        else: return (a,b-1)
    elif b==y:
        if a<x: return (a+1,b)
        else: return (a-1,b)
    elif a<x and b<y:
        return (a+1,b+1)
    elif a<x and b>y:
        return (a+1,b-1)
    elif a>x and b<y:
        return (a-1,b+1)
    elif a>x and b>y:
        return (a-1,b-1)
    
        

n,m=map(int,input().split())

adu=[]
count=[[0]*m for i in range(n)]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='I': x,y=i,j
        elif temp[j]=='R':
            adu.append([i,j])
            count[i][j]+=1
N=len(adu)
dead=[0]*N

cmd=list(map(lambda x: int(x)-1,input()))

finish=0
t=0
for c in cmd:
    t+=1
    x,y=x+dx[c],y+dy[c]
    if count[x][y]:
        finish=1
        break
        
    for i in range(N):
        if dead[i]: continue
        a,b=adu[i]
        na,nb=nextMove(a,b)
        count[a][b]-=1
        count[na][nb]+=1
        adu[i]=[na,nb]
    if count[x][y]:
        finish=1
        break
    temp=[]
    for i in range(N):
        a,b=adu[i]
        if count[a][b]>1:
            temp.append(i)
            dead[i]=1
    for i in temp:
        a,b=adu[i]
        count[a][b]=0

if not finish:
    board=[['.']*m for i in range(n)]
    board[x][y]='I'
    for i in range(N):
        if dead[i]:continue
        a,b=adu[i]
        board[a][b]='R'
    for i in range(n):
        print(''.join(board[i]))

else:
    print(f'kraj {t}')
