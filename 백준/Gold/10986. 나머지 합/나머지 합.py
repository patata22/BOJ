n,m=map(int,input().split())
number=[0]+list(map(int,input().split()))
pre=[0]*(n+1)
cnt=[0]*m
for i in range(1,n+1):
    pre[i]=(pre[i-1]+number[i])%m
for i in range(n+1):
    cnt[pre[i]]+=1
answer=0
for i in range(m):
    t=cnt[i]
    answer+=t*(t-1)//2
print(answer)
