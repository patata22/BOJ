n,m=map(int,input().split())

basket = [i for i in range(n+1)]

for _ in range(m):
    i,j,k=map(int,input().split())

    for __ in range(k-i):
        basket.insert(j,basket.pop(i))

print(*basket[1:])
