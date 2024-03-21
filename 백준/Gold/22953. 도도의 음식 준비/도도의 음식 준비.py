import sys
input=sys.stdin.readline

def bs():
    l=0
    r=10**12
    while l+1<r:
        mid=(l+r)//2
        total=0
        for t in time:
            total+=mid//t

        if total>=k: r=mid
        else:l=mid
    return r

def sol(depth):
    if depth==c:
        global answer
        answer=min(answer,bs())
        return
    change=0
    for i in range(n):
        if time[i]>1:
            time[i]-=1
            change=1
            sol(depth+1)
            time[i]+=1
    if not change: sol(c)

n,k,c=map(int,input().split())
time=list(map(int,input().split()))
answer=float('inf')
sol(0)
print(answer)
