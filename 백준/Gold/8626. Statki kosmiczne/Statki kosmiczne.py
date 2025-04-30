import sys
input=sys.stdin.readline

def sol(a,b):
    l=-1
    r=c+1
    while l+1<r:
        mid=(l+r)//2
        if (a+b+C[mid])*2>MAX: r=mid
        else: l=mid
    return c-r

B,K,Z=map(int,input().split())

a=int(input())
A=list(map(lambda x: int(x)*B,input().split()))
b=int(input())
B=list(map(lambda x: int(x)*K,input().split()))
c=int(input())
C=list(map(lambda x: int(x)*Z,input().split()))

A.sort()
B.sort()
C.sort()
MAX=A[-1]+B[-1]+C[-1]
C.append(float('inf'))

answer=0
for i in range(a):
    for j in range(b):
        answer+=sol(A[i],B[j])

print(answer)