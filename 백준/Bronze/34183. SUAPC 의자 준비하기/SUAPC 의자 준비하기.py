n,m,a,b=map(int,input().split())

need=max(0,3*n-m)
if need: print(a*need+b)
else: print(0)

    