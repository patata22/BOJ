for _ in range(int(input())):
    a,b=map(int,input().split())
    a-= b//7-b//4
    print(a)
