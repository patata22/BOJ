n=int(input())
number=list(map(int,input().split()))

answer=[]
small=float('inf')
before=0
gap=0
for i in range(n):
    now=number[i]
    if small>now: small=now
    else:gap=max(gap,now-small)
    answer.append(gap)
print(*answer)