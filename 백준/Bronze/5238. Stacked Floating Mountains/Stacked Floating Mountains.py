for _ in range(int(input())):
    c=0
    n=list(map(int,input().split()))
    for i in range(3,len(n)):
        if n[i]!=n[i-1]+n[i-2]:c=1
    print('YNEOS'[c::2])
