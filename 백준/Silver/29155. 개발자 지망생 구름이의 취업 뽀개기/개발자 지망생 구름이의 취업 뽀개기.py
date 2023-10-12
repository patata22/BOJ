n=int(input())
p=[0]+list(map(int,input().split()))
test=[[] for i in range(6)]
for _ in range(n):
    a,b=map(int,input().split())
    test[a].append(b)
for i in range(6):
    test[i].sort(reverse=True)

answer=-60
for i in range(1,6):
    if p[i]: answer+=60
    answer+=test[i][-1]
    before=test[i].pop()
    for j in range(p[i]-1):
        answer+=test[i][-1]-before
        before=test[i].pop()
        answer+=before

print(answer)