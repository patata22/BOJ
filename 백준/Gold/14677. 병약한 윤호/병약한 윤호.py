from collections import deque

def sol():
    q=deque()
    t=0
    if drug[0]=='B':
        q.append(('L',1,0))
        visited[1][0]=1
    if drug[-1]=='B':
        q.append(('L',0,1))
        visited[0][1]=1
    while q:
        for _ in range(len(q)):
            target,left,right=q.popleft()
            if left+right==3*n:continue
            if drug[left]==target and left<3*n-1 and not visited[left+1][right]:
                visited[left+1][right]=1
                q.append((next[target], left+1, right))
            if drug[3*n-1-right]==target and right<3*n-1 and not visited[left][right+1]:
                visited[left][right+1]=1
                q.append((next[target], left, right+1))
        t+=1
    return t
n=int(input())
drug=list(input())
next={'B':'L','L':'D','D':'B'}
visited=[[0]*(3*n) for i in range(3*n)]
print(sol())
