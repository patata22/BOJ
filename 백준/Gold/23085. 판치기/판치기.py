from collections import deque

def sol():
    n,k=map(int,input().split())
    x=input().count('H')
    q=deque()
    q.append(x)
    visited=[0]*(n+1)
    visited[x]=1
    T=0
    while q:
        for _ in range(len(q)):
            h=q.popleft()
            if not h: return T
            t=n-h
            for i in range(k+1):
                hflip = i
                tflip = k-i
                if hflip>h or tflip>t: continue
                nh = h-hflip+tflip
                nt = t-tflip+hflip
                if 0<=nh<=n and 0<=nt<=n and not visited[nh]:
                    visited[nh]=1
                    q.append(nh)

        T+=1
    return -1
print(sol())
            
             