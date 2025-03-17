input()
now=list(map(int,input().split()))
nxt=[]
while len(now)>1:
    for i in range(len(now)-1):
        nxt.append(now[i]+now[i+1])
    print(*nxt)
    now=nxt
    nxt=[]
