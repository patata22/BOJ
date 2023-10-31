n,m=map(int,input().split())
number=list(map(int,input().split()))
friend=set(map(int,input().split()))
answer=0
for i in range(m):
    if number[i] not in friend: answer+=1
print(answer)
