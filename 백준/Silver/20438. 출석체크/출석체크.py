import sys
input=sys.stdin.readline


n,k,q,m=map(int,input().split())

sleep=set(map(int,input().split()))
qr=list(map(int,input().split()))
answer=[0]*(n+3)

for x in qr:
    if x in sleep: continue
    for i in range(x,n+3,x):
        answer[i]=1
for x in sleep: answer[x]=0

for i in range(1,n+3): answer[i]+=answer[i-1]


A=[]
for _ in range(m):
    a,b=map(int,input().split())
    temp=answer[b]-answer[a-1]
    A.append(str(b-a+1-temp))

print('\n'.join(A))
