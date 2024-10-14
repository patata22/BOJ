n,b=map(int,input().split())
g=1-b
gg,gb,bg,bb = map(float,input().split())

for _ in range(n):
    g,b = gg*g+bg*b, gb*g+bb*b
g= round(g*1000+0.0001)
b= round(b*1000+0.0001)
print(g)
print(b)

