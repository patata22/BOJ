n,m=map(int,input().split())

x=0
temp=float('inf')
for i in range(n-1):
    X=int(input())
    if X<temp:
        temp=X
        x=i+1
number=list(map(int,input().split()))
if number[0]<temp:
    x=n
temp=float('inf')
for i in range(m):
    if number[i]<temp:
        temp=number[i]
        y=i+1
print(x,y)
    
      