from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def toString(board):
    temp=''
    for i in range(4):
        temp+=''.join(board[i])
    return temp

def sol():
    q=deque()
    q.append(board)
    visited.add(toString(board))
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if toString(now)==final: return t
            for x in range(4):
                for y in range(4):
                    for i in range(4):
                        temp = [now[j][:] for j in range(4)]
                        nx,ny=x+dx[i],y+dy[i]
                        if 0<=nx<4 and 0<=ny<4:
                            temp[x][y],temp[nx][ny]=temp[nx][ny],temp[x][y]
                            if toString(temp) not in visited:
                                visited.add(toString(temp))
                                q.append(temp)
        t+=1
    

board=[list(input()) for i in range(4)]
end=[]
while True:
    x=list(input())
    if x:
        end.append(x)
        break
for _ in range(3): end.append(list(input()))

final = toString(end)
visited=set()

print(sol())
