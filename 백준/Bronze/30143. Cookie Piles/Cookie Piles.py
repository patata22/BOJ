for tt in range(int(input())):
    a,b,c=map(int,input().split())
    print(sum([i for i in range(b, b+a*c,c)]))
