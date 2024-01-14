dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(maze):    
    n=len(maze)
    m=len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j]==1:rx,ry=i,j
            elif maze[i][j]==2: bx,by=i,j
            elif maze[i][j]==3: erx,ery=i,j
            elif maze[i][j]==4: ebx,eby=i,j

    visited_red=[[0]*m for i in range(n)]
    visited_blue=[[0]*m for i in range(n)]
    visited_red[rx][ry]=1
    visited_blue[bx][by]=1

    answer=float('inf')

    def sol(depth,rx,ry,bx,by):
        nonlocal erx,ery,ebx,eby,answer
        if depth>=answer: return
        if rx==erx and ry==ery and bx==ebx and by==eby:
            answer=min(answer,depth)
            return
        temp_red=[]
        if rx==erx and ry==ery:
            temp_red.append((rx,ry))
        else:
            for i in range(4):
                nrx,nry=rx+dx[i],ry+dy[i]
                if 0<=nrx<n and 0<=nry<m and maze[nrx][nry]!=5 and not visited_red[nrx][nry]:
                    temp_red.append((nrx,nry))
        temp_blue=[]
        if bx==ebx and by==eby:
            temp_blue.append((bx,by))
        else:
            for i in range(4):
                nbx,nby=bx+dx[i],by+dy[i]
                if 0<=nbx<n and 0<=nby<m and maze[nbx][nby]!=5 and not visited_blue[nbx][nby]:
                    temp_blue.append((nbx,nby))
        nxt=[]
        for nrx,nry in temp_red:
            for nbx,nby in temp_blue:
                nxt.append((nrx,nry,nbx,nby))

        for nrx,nry,nbx,nby in nxt:
            if nrx==nbx and nry==nby: continue
            if nrx==bx and nry==by and nbx==rx and nby==ry:continue
            visited_red[nrx][nry]=1
            visited_blue[nbx][nby]=1
            sol(depth+1, nrx,nry,nbx,nby)
            visited_blue[nbx][nby]=0
            visited_red[nrx][nry]=0
            
        
    sol(0,rx,ry,bx,by)
    if answer==float('inf'):return 0
    return answer