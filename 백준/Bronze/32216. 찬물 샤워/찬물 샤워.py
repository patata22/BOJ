n,k,t=map(int,input().split())
d=tuple(map(int,input().split()))

answer=0
for x in d:
    if t>k:t=t+x-abs(t-k)
    else: t= t+x+abs(t-k)
    answer+=abs(t-k)

print(answer)
