for tt in range(int(input())):
    now=1
    for _ in range(1,int(input())+1):
        now*=_
    print(now%10)
