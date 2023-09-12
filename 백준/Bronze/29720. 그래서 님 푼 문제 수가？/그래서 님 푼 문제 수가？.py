n,m,k=map(int,input().split())
mi = n-m*k
ma = mi+m-1
print(max(0,mi),ma)

