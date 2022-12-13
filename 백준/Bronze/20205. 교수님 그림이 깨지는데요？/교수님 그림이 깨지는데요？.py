n,k=map(int,input().split())

for i in range(n):
    temp = list(map(int,input().split()))
    new = []
    for x in temp:
        for j in range(k):
            new.append(x)
    for j in range(k):
        print(*new)
