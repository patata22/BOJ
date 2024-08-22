for tt in range(int(input())):
    g,c,e=map(int,input().split())
    need=max(0,e-c)
    g=2*g-1
    print(g*need)
