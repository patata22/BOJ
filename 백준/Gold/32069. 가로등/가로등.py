from collections import deque

def sol():
    l,n,k=map(int,input().split())
    q=deque(map(int,input().split()))
    visited=set()
    for x in q:
        visited.add(x)
    light=0
    cnt=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            print(light)
            cnt+=1
            if cnt==k: return
            if 0<=now-1 and now-1 not in visited:
                visited.add(now-1)
                q.append(now-1)
            if now+1<=l and now+1 not in visited:
                visited.add(now+1)
                q.append(now+1)
                
        light+=1

sol()
