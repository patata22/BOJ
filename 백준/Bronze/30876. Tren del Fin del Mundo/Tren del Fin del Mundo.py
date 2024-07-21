x=0
y=float('inf')
for _ in range(int(input())):
    a,b=map(int,input().split())
    if b<y:
        y=b
        x=a
print(x,y)
