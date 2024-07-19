import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        p[a]+=p[b]
        p[b]=a
        candy[a]+=candy[b]
        candy[b]=0

n,m,k=map(int,input().split())

p=[-1]*n
candy=list(map(int,input().split()))

for _ in range(m):
    a,b=map(lambda x: int(x)-1,input().split())
    union(a,b)

group=[]
for i in range(n):
    if p[i]<0:
        group.append(i)

n=len(group)

dp=[[0]*k for i in range(n+1)]
for i in range(1,n+1):
    w,v = -p[group[i-1]],candy[group[i-1]]
    for j in range(k):
        if j<w: dp[i][j]= dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[-1][-1])
                             
