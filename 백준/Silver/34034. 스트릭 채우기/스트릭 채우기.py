def sol():
    global m
    now=-1
    while number and now<k-1:
        idx,need=number.pop()
        idx+=1
        if need-1>m: return 0
        m-=need-1
        now+=need-1
        if now>=k-1: return 1
        now+=1
        answer[now]=idx
        if now+m>=k-1: return 1
    return 1
        
    

n,m,k=map(int,input().split())
number=sorted(enumerate(map(int,input().split())),key=lambda x: x[1],reverse=True)
answer=[0]*k
if sol(): print(*answer)
else: print(-1)
