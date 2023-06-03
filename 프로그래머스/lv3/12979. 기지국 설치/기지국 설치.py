from collections import deque

def solution(n, stations, w):
    q=deque()
    q.append((0,0))
    answer = 0
    for station in stations:
        s=max(1,station-w)
        e=min(n,station+w)
        q.append((s,e))
    q.append((n+1,n+1))
    w=2*w+1
    while q:
        s,e=q.popleft()
        if not q: break
        S,E=q[0]
        temp=S-1-e
        answer+=temp//w     
        if temp%w: answer+=1

    return answer