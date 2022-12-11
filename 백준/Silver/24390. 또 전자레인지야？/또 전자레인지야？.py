from collections import deque

dt = ((10,60,600), (10,30,60,600))

def sol():
    q=deque()
    q.append((0,0))
    t=0
    while q:
        for _ in range(len(q)):
            now,started = q.popleft()
            if now==second and started: return t
            if not started:
                if not now: q.append((30,1))
                elif not visited[now][1]:
                    q.append((now,1))
                for d in dt[0]:
                    nx = now+d
                    if 0<=nx<=3600 and not visited[nx][0]:
                        visited[nx][0]=1
                        q.append((nx,0))
            else:
                for d in dt[1]:
                    nx = now+d
                    if 0<=nx<=3600 and not visited[nx][1]:
                        visited[nx][1]=1
                        q.append((nx,1))
                
        t+=1
        
m,s = map(int,input().split(":"))
second = 60*m+s
visited=[[0]*2 for i in range(3601)]
print(sol())
