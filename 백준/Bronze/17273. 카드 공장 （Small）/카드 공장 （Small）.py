n,m=map(int,input().split())
a,b=map(int,input().split())
for _ in range(m):
    if int(input())>=a:
        a,b=b,a
print(a)
