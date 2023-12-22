time=[0]*1001
guard=[tuple(map(int,input().split())) for i in range(int(input()))]
for a,b in guard:
    for i in range(a,b):time[i]+=1

answer=0
for a,b in guard:
    for i in range(a,b):time[i]-=1
    answer=max(1001-time.count(0),answer)
    for i in range(a,b):time[i]+=1
print(answer)
    
