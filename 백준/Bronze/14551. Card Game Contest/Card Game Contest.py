def parse(x):
    x=int(x)
    if not int(x): return 1
    return x

n,m=map(int,input().split())

answer=1
for _ in range(n):
    answer=answer*parse(input())
print(answer%m)
