n,k=map(int,input().split())

save = 0
now = 0

for _ in range(n):
    cmd=input()
    if cmd=='save': save=now
    elif cmd=='load': now=save
    elif cmd=='shoot': now-=1
    else: now+=k
    print(now)
    
