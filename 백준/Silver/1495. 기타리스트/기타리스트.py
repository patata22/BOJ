n,s,m=map(int,input().split())
V=list(map(int,input().split()))

q=set()
q.add(s)
for i in range(n):
    nxt=set()
    nxt.add(-1)
    for x in q:
        if x==-1: continue
        if 0<=x-V[i]<=m: nxt.add(x-V[i])
        if 0<=x+V[i]<=m: nxt.add(x+V[i])
    q=nxt
print(max(q))