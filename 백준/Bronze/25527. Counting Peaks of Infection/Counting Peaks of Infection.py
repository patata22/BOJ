while True:
    n=int(input())
    if not n: break
    ans=0
    down=0
    num=tuple(map(int,input().split()))
    now=num[0]
    for i in range(1,n):
        if num[i]<now:
            if not down:ans+=1
            down=1
        else: down=0
        now=num[i]
        
    print(ans)
