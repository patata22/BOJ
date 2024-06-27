n,m=map(int,input().split())

answer=1
for i in range(1,n+1):
    answer=(answer*i)%m
print(answer)
