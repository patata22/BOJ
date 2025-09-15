from collections import deque

da=[-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
db=[0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dc=[0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd=[0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
de=[0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0]
df=[0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0]
dg=[0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0]
dh=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0]
di=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0]
dj=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0]
dk=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]

def bfs(start):
    deq=deque(start)
    while deq:
        k,j,i,h,g,f,e,d,c,b,a,time=deq.popleft()
        for z in range(22):
            na, nb, nc, nd, ne, nf, ng,nh,ni,nj,nk= a+da[z], b+db[z], c+dc[z], d+dd[z], e+de[z], f+df[z], g+dg[z], h+dh[z], i+di[z], j+dj[z], k+dk[z]
            if 0<=na<m and 0<=nb<n and 0<=nc<o and 0<=nd<p and 0<=ne<q and 0<=nf<r and 0<=ng<s and 0<=nh<t and 0<=ni<u and 0<=nj<v and 0<=nk<w and board[nk][nj][ni][nh][ng][nf][ne][nd][nc][nb][na]==0:
                board[nk][nj][ni][nh][ng][nf][ne][nd][nc][nb][na]=1
                deq.append((nk,nj,ni,nh,ng,nf,ne,nd,nc,nb,na, time+1))
    return time


m,n,o,p,q,r,s,t,u,v,w=map(int,input().split())
board=[[[[[[[[[[list(map(int,input().split())) for i in range(n)] for i in range(o)] for i in range(p)] for i in range(q)] for i in range(r)] for i in range(s)] for i in range(t)] for i in range(u)] for i in range(v)] for i in range(w)]
start=[]
for a in range(m):
    for b in range(n):
        for c in range(o):
            for d in range(p):
                for e in range(q):
                    for f in range(r):
                        for g in range(s):
                            for h in range(t):
                                for i in range(u):
                                    for j in range(v):
                                        for k in range(w):
                                            if board[k][j][i][h][g][f][e][d][c][b][a]==1:start.append((k,j,i,h,g,f,e,d,c,b,a,0))
                                            
if not start:print(-1)
else:
    answer=bfs(start)
    good=1
    for a in range(m):
        for b in range(n):
            for c in range(o):
                for d in range(p):
                    for e in range(q):
                        for f in range(r):
                            for g in range(s):
                                for h in range(t):
                                    for i in range(u):
                                        for j in range(v):
                                            for k in range(w):
                                                if board[k][j][i][h][g][f][e][d][c][b][a]==0:
                                                    good=0
                                                    break
                                        
    if not good: print(-1)                                            
    else:print(answer)


                                    
