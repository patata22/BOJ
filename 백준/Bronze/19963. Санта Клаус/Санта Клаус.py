n,m,k=map(int,input().split())
answer=[0]*(n+1)
for _ in range(2):
    for x in list(map(int,input().split())):
        answer[x]=1
print(n-m-k)
for i in range(1,n+1):
    if not answer[i]: print(i, end=' ')
