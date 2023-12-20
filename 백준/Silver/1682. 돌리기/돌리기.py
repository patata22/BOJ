from collections import deque

def sol():
    q=deque()
    q.append((1,2,3,4,5,6,7,8))
    visited=set()
    visited.add((1,2,3,4,5,6,7,8))
    target=tuple(map(int,input().split()))
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now==target: return t
            a,b,c,d,e,f,g,h=now
            x=(h,g,f,e,d,c,b,a)
            if x not in visited:
                q.append(x)
                visited.add(x)
            x=(d,a,b,c,f,g,h,e)
            if x not in visited:
                q.append(x)
                visited.add(x)
            x=(a,c,f,d,e,g,b,h)
            if x not in visited:
                q.append(x)
                visited.add(x)
            x=(e,b,c,d,a,f,g,h)
            if x not in visited:
                q.append(x)
                visited.add(x)
        t+=1

print(sol())
