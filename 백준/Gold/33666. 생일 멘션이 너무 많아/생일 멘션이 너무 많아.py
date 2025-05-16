def sol():
    avg=total//cnt
    answer=[0]*(m+1)
    for x in number:
        if m<x<=avg: return [-1]
        answer[0]+=1
        if x>avg: answer[1]-=1
        else:
            if x%m: answer[x%m]-=1
    for i in range(1,m+1):
        answer[i]+=answer[i-1]
    answer.pop()
    return answer

n,m=map(int,input().split())
number=list(map(int,input().split()))
cnt=0
total=0

for x in number:
    if x>1:
        cnt+=1
        total+=x

if not total:
    answer=[0]*m
    answer[0]=n
    print(*answer)
else:print(*sol())
