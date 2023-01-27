for _ in range(int(input())):
    n,m=map(int,input().split())

    count=[0]*n

    for __ in range(m):
        temp=list(map(int,input().split()))
        for j in range(n):
            count[j]+=temp[j]
    print(count.index(max(count))+1)