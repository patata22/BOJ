import sys
input=sys.stdin.readline

n,m=map(int,input().split())
answer=[0]
total=sum(map(int,input().split()))
team=[]

for _ in range(n):
    temp=sum(map(int,input().split()))
    if temp>total: continue
    team.append((temp,_))

team.sort(key=lambda x: -x[0])
for _ in range(min(len(team),m-1)):
    answer.append(team[_][1]+1)
print(*answer)
