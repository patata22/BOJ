mi=float('inf')
ma=-float('inf')
for _ in range(int(input())):
    a,b=map(int,input().split())
    mi=min(mi,b)
    ma=max(ma,b)
print(ma-mi)
