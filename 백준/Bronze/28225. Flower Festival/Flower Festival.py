n,f=map(int,input().split())
time=float('inf')
answer=0
for i in range(1,n+1):
    a,b=map(int,input().split())
    t=(f-a)/b
    if t<time:
        time=t
        answer=i
print(answer)
