for tt in range(int(input())):
    input()
    a,b,c,d=map(int,input().split())
    temp=[a,b,c]
    for _ in range(d):
        temp.sort()
        temp[-1]-=1
    a,b,c=temp
    print(a*b*c)
