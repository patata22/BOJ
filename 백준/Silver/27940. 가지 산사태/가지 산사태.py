import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
water=0
flag=True
for _ in range(m):
     a,b=map(int,input().split())
     water+=b
     if water>k:
         print(_+1, 1)
         flag=False
         break
if flag:print(-1)
