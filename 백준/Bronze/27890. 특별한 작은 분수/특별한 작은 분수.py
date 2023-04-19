x,n=map(int,input().split())
for i in range(n):
    if x%2: x= (x<<1)^6
    else: x= (x>>1)^6
print(x)
   