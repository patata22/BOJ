N,m,M,T,R = map(int,input().split())

time=0
cnt=0
beat=m
if m+T>M:print(-1)
else:
    while cnt<N:
        time+=1
        if beat+T>M:
            beat=max(m,beat-R)
        else:
            cnt+=1
            beat+=T
    print(time)
