n=int(input())
before=tuple(map(int,input().split()))
rank={}
for i in range(n):
    rank[before[i]]=i
after=tuple(map(int,input().split()))
gap=0
answer=[]
for i in range(n):
    temp=rank[after[i]]-i
    if temp>gap:
        gap=temp
        answer=[after[i]]
    elif temp==gap:
        answer.append(after[i])
print(*answer)