t=0
b=float('inf')

for _ in range(int(input())):
    a,c=map(int,input().split())
    t=max(t,a)
    b=min(b,c)

print((t*b)%7+1)
