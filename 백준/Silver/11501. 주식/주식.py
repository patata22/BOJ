for _ in range(int(input())):
    n=int(input())
    stock=list(map(int,input().split()))
    answer=0
    high=0
    while stock:
        now=stock.pop()
        if now>high:
            high=now
        else:
            answer+=high-now
    print(answer)
        

