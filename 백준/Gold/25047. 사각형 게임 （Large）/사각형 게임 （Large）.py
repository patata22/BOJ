def w(d):
    if d==n:
        global a
        a=max(a,j())
        return
    w(d+1)
    r[d]=1
    w(d+1)
    r[d]=0
def j():
    t=0
    for j in range(n):
        s=0
        A=[0,0]
        for i in range(n):
            A[r[i]]+=b[i][j]
            s+=b[i][j]
        t+=s-max(A)
    return t
n=int(input())
b=[list(map(int,input().split())) for i in range(n)]
r=[0]*n
a=-float('inf')
w(0)
print(a)