n,a,b=map(int,input().split())
g=1
c=1
for _ in range(n):
    g+=a
    c+=b
    if c>g: g,c=c,g
    elif c==g: c-=1

print(g,c)
