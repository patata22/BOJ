n=int(input())
speed=list(map(int,input().split()))
answer=0
now=0
while speed:
    now=min(now+1, speed.pop())
    answer+=now
print(answer)

