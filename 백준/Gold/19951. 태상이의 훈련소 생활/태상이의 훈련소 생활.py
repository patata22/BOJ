import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=list(map(int,input().split()))
arr=[0]*(n+1)
for _ in range(m):
    a,b,k=map(int,input().split())
    a-=1
    arr[a]+=k
    arr[b]-=k
for i in range(1,n):
    arr[i]+=arr[i-1]
    number[i]+=arr[i]
number[0]+=arr[0]
print(*number)