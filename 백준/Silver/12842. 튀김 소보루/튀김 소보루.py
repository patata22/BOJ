import sys,heapq
input=sys.stdin.readline

n,s=map(int,input().split())
eat=n-s
time=[0]*(n+1)
q=[]
for i in range(1,int(input())+1):
    heapq.heappush(q,(0,i,int(input())))

count=0
while count<eat:
    count+=1
    if count==eat:
        print(heapq.heappop(q)[1])
        break
    time, number, speed = heapq.heappop(q)
    heapq.heappush(q,(time+speed, number, speed))
