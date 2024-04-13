from collections import deque

def bfs(x):
    q=deque()
    q.append(0)
    visited=[0]*n
    visited[0]=1
    while q:
        now=q.popleft()
        if now==n-1: return True
        for i in range(now+1, n):
            if not visited[i] and (i-now)*(1+abs(number[i]-number[now]))<=x:
                visited[i]=1
                q.append(i)
    return False

def sol():
    l=0
    r=10**12
    while l+1<r:
        mid=(l+r)//2
        if bfs(mid): r=mid
        else: l=mid
    return r

n=int(input())
number=list(map(int,input().split()))
print(sol())
