n,m=map(int,input().split())
fence=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        fence[i]=1
print('YES') if sum(fence)==n else print('NO')
