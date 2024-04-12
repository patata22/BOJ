def sol(x):
    l=0
    r=n+2
    while l+1<r:
        mid=(l+r)//2
        if p[mid]>=x: l=mid
        else: r=mid
    return l

n=int(input())
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))
size=[A[i]-B[i] for i in range(n)]
p=[float('inf')]
for i in range(n):
    p.append(min(p[-1],size[i]))
p.append(-float('inf'))
input()
for x in map(int,input().split()):
    print(sol(x))

