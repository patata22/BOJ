dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)


def springAndSummer():
    for i in range(n):
        for j in range(n):
            tree[i][j].sort(reverse=True)
            nxt=[]
            dead=0
            while tree[i][j]:
                now=tree[i][j].pop()
                if nutrient[i][j]>=now:
                    nutrient[i][j]-=now
                    nxt.append(now+1)
                    if now%5==4:
                        newtree[i][j]+=1
                else:
                    dead+=now//2
            tree[i][j]=nxt
            nutrient[i][j]+=dead

def fall():
    for x in range(n):
        for y in range(n):
            if newtree[x][y]:
                for d in range(8):
                    nx,ny=x+dx[d],y+dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        for k in range(newtree[x][y]):
                            tree[nx][ny].append(1)
            newtree[x][y]=0

def winter():
    for x in range(n):
        for y in range(n):
            nutrient[x][y]+=s2d2[x][y]
                
n,m,k=map(int,input().split())
tree=[[[] for i in range(n)] for i in range(n)]
newtree=[[0]*n for i in range(n)]
s2d2=[tuple(map(int,input().split())) for i in range(n)]
nutrient=[[5]*n for i in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    tree[a-1][b-1].append(c)

for i in range(k):
    springAndSummer()
    fall()
    winter()
answer=0
for i in range(n):
    for j in range(n):
        answer+=len(tree[i][j])
print(answer)
