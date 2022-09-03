n,m,k=map(int,input().split())
sand=list(map(int,input().split()))
stone=list(map(lambda x: int(x)-1,input().split()))

pre=[]
for i in range(k-1):
    now,nxt = stone[i],stone[i+1]
    pre.append((sum(sand[now:nxt]),now))
pre.append((sum(sand[stone[k-1]:]),stone[k-1]))
pre.sort(key=lambda x: (-x[0],x[1]))
answer=[]
for i in range(m):answer.append(pre[i][1])
answer.sort()
for x in answer:print(x+1)