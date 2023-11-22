n=int(input())
time=[0]*1001
answer='edward is right'
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b+1):time[i]+=1
for x in time:
    if x==n:answer='gunilla has a point'
print(answer)