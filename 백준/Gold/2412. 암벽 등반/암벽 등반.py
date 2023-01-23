from collections import deque
import sys
input=sys.stdin.readline

dx=[]
dy=[]

for i in range(-2,3):
    for j in range(-2,3):
        if not i and not j: continue
        dx.append(i)
        dy.append(j)


def sol():
    q=deque()
    q.append((0,0))
    visited=set()
    visited.add((0,0))
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if y==T: return t
            for i in range(24):
                nx,ny=x+dx[i],y+dy[i]
                if (nx,ny) in stone and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny))
        t+=1
    return -1
n,T=map(int,input().split())
vistied=set()
stone=set()
for i in range(n):
    stone.add(tuple(map(int,input().split())))

print(sol())
