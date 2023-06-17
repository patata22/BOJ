n,m=map(int,input().split())
satis=sorted(list(map(int,input().split())),reverse=True)
cost=sorted(list(map(int,input().split())))
answer=0
for i in range(min(n,m)):
    temp=satis[i]-cost[i]
    if temp>0:answer+=temp

print(answer)
    
