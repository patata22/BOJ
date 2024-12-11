from collections import deque

def sol2():
    x,y=map(int,input().split())
    q=deque()
    q.append((x,y))
    visited=[[0]*61 for i in range(61)]
    visited[x][y]=1
    t=0
    damage=((9,3),(3,9))
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if not x and not y: return t
            for dx,dy in damage:
                nx,ny=max(0,x-dx),max(0,y-dy)
                if not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1

def sol3():
    x,y,z=map(int,input().split())
    q=deque()
    q.append((x,y,z))
    visited=[[[0]*61 for i in range(61)] for i in range(61)]
    visited[x][y][z]=1
    t=0
    damage=((1,3,9),(1,9,3),(3,1,9),(3,9,1),(9,1,3),(9,3,1))
    while q:
        for _ in range(len(q)):
            x,y,z=q.popleft()
            if not x and not y and not z: return t
            for dx,dy,dz in damage:
                nx,ny,nz=max(0,x-dx),max(0,y-dy),max(0,z-dz)
                if not visited[nx][ny][nz]:
                    visited[nx][ny][nz]=1
                    q.append((nx,ny,nz))
        t+=1
    

n=int(input())
if n==1:
    hp=int(input())
    answer=hp//9
    if hp%9: answer+=1
    print(answer)

elif n==2:
    print(sol2())
else:
    print(sol3())
