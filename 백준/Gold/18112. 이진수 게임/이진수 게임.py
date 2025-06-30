from collections import deque

def getNext(x):
    result=[]
    l=len(bin(x)[3:])
    for i in range(-1,-l,-1):
        result.append(x^(1<<-i))
    if x!=0: result.append(x-1)
    if x<2047:result.append(x+1)
    return result
    
def sol():
    s,e=int(input(),2),int(input(),2)
    visited=[0]*(2**11)
    q=deque()
    q.append(s)
    visited[s]=1
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now==e: return t
            for x in getNext(now):
                if not visited[x]:
                    visited[x]=1
                    q.append(x)
        t+=1
    
print(sol())
