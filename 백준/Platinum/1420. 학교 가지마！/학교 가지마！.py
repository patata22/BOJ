from collections import deque,defaultdict
import sys
input=sys.stdin.readline

dx=(1,0)
dy=(0,1)

def sol():
    total=0
    while True:
        q=deque()
        prev=[-1]*TOTAL
        q.append(START)
        while q:
            now=q.popleft()
            for to in graph[now]:
                if prev[to]==-1 and capa[now][to]>0:
                    prev[to]=now
                    q.append(to)
                    if to==END:break
        if prev[END]==-1: break
        total+=1
        now=END
        while now!=START:
            capa[prev[now]][now]-=1
            capa[now][prev[now]]+=1
            now=prev[now]
    return total    

n,m=map(int,input().split())
TOTAL=2*n*m
board=[]
graph=[[] for i in range(TOTAL)]
capa=[defaultdict(int) for i in range(TOTAL)]
count=0
for i in range(n):
    temp=list(input().rstrip())
    for j in range(m):
        if temp[j]=='K':
            START=2*(i*m+j)+1
            sx,sy=i,j
            temp[j]='.'
        elif temp[j]=='H':
            END=2*(i*m+j)
            ex,ey=i,j
            temp[j]='.'
    board.append(temp)

for x in range(n):
    for y in range(m):
        if board[x][y]=='#': continue
        one=2*(m*x+y)
        two=one+1
        graph[one].append(two)
        graph[two].append(one)
        capa[one][two]=1
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
                three=2*(m*nx+ny)
                four=three+1
                graph[two].append(three)
                graph[three].append(two)
                capa[two][three]=float('inf')                
                graph[four].append(one)
                graph[one].append(four)
                capa[four][one]=float('inf')
if abs(sx-ex)+abs(sy-ey)==1:
    print(-1)
else:print(sol())
