n,k=map(int,input().split())
number=sorted(list(map(int,input().split())))

used=[0]*(n+1)
answer=1
for i in range(n):
    if number[i]>i+1:
        answer=0
        break
    p=False
    for j in range(number[i],n+1,k):
        if not used[j]:
            used[j]=1
            p=True
            break
    if not p:
        answer=0
        break
print(answer)
