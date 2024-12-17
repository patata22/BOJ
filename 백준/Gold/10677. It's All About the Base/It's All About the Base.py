def change(n,x):
    result=0
    mul=1
    while n:
        result +=(n%10)*mul
        n//=10
        mul*=x
    return result

def sol():
    for i in range(10,15001):
        A=change(a,i)
        success,result=check(A,i)
        if success: return i,result

def check(A,n):
    l=10
    r=15001
    while l+1<r:
        mid=(l+r)//2
        result=change(b,mid)
        if result==A: return True, mid
        elif result<A: l=mid
        else: r=mid
    return False, -1
    

for tt in range(int(input())):
    a,b=map(int,input().split())
    print(*sol())
