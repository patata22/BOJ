from collections import deque
dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(land, height):
    answer = 0
    
    n=len(land)
    board=[[0]*n for i in range(n)]
    visited=[[0]*n for i in range(n)]
    level=0
    
    def fill(i,j,level):
        q=deque()
        q.append((i,j))
        board[i][j]=level
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and abs(land[x][y]-land[nx][ny])<=height:
                    board[nx][ny]=level
                    visited[nx][ny]=1
                    q.append((nx,ny))
        
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j]=1
                level+=1
                fill(i,j,level)
    
    graph=[]
    visited=[[0]*n for i in range(n)]
    
    def findGraph(i,j):
        start=board[i][j]
        tempGraph={}
        q=deque()
        q.append((i,j))
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny]==start and not visited[nx][ny]:
                        visited[nx][ny]=1
                        q.append((nx,ny))
                    elif board[nx][ny]!=start:
                        to=board[nx][ny]
                        if to in tempGraph:
                            tempGraph[to]=min(tempGraph[to], abs(land[x][y]-land[nx][ny]))
                        else:
                            tempGraph[to]=abs(land[x][y]-land[nx][ny])
        
        for to in tempGraph:
            graph.append((start,to,tempGraph[to]))
        return
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j]=1
                findGraph(i,j)
    graph.sort(key=lambda x: x[2])
    
    p=[-1]*(level+1)
    def find(a):
        if p[a]<0: return a
        p[a]=find(p[a])
        return p[a]
    
    def union(a,b):
        pa,pb=find(a),find(b)
        if pa!=pb:p[b]=pa
        
    def kruskal():
        answer=0
        cnt=0
        for i in range(len(graph)):
            start, end, cost= graph[i]
            a,b=find(start), find(end)
            if a!=b:
                cnt+=1
                answer+=cost
                union(a,b)
                if cnt==level-1: break
        return answer
            
    return kruskal()
    