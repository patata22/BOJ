import sys
input=sys.stdin.readline

n,m=map(int,input().split())
point=[tuple(map(int,input().split())) for i in range(m)]
group=[[] for i in range(n)]
for x in point:
    for i in range(n):
        group[i].append(x[i])
for i in range(n):
    group[i].sort()

ap=[]
for i in range(n): ap.append(group[i][m//2])
total=0
for i in range(n):
    temp=group[i]
    total+=sum(map(lambda x: abs(x-ap[i]),temp))
print(total)
print(*ap)
