DIV=10**9+7

n=int(input())
a,b=1,1
for i in range(2,n):
    a,b=b,(a+b)%DIV
print(b,n-2)