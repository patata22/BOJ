from collections import deque

def sol():
    input()
    q=deque()
    visited=[0]*360
    for x in map(int,input().split()):
        q.append(x)
        visited[x]=1
    while q:
        now=q.popleft()
        for i in range(360):
            if visited[i]:
                if not visited[(now+i)%360]:
                    visited[(now+i)%360]=1
                    q.append((now+i)%360)
                if not visited[(now-i)%360]:
                    visited[(now-i)%360]=1
                    q.append((now-i)%360)
        

    for x in map(int,input().split()):
        if visited[x]: print('YES')
        else: print('NO')

sol()