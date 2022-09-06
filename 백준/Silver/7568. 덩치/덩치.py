n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
for x in lst:
    rank=1
    for y in lst:
        if x[0]<y[0] and x[1]<y[1]:rank+=1
    print(rank, end=' ')