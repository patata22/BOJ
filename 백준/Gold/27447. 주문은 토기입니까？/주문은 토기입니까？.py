n,m=map(int,input().split())
number=list(map(int,input().split()))
t=0
target=0
nxt=0
cup=0
coffee=0
answer='success'
while target<n:
    if t==number[target]:
        if not coffee:
            answer='fail'
        coffee-=1
        target+=1
    elif t+m>=number[nxt]:
        if not cup: cup+=1
        else:
            cup-=1
            coffee+=1
            if nxt!=n-1:nxt+=1
    else:cup+=1
    t+=1
    
print(answer)
