w,n=map(int,input().split())
p=list(map(int,input().split()))
answer=set()
answer.add(w)
for i in range(n):
    x=p[i]
    answer.add(x)
    answer.add(w-x)
    for j in range(i+1,n):
        y=p[j]
        answer.add(y-x)

print(*sorted(list(answer)))
