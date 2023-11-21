n,s=map(int,input().split())
speed=0
for _ in range(n-1):
    x=int(input())
    speed+=x
    if speed>s:speed-=1
speed+=int(input())
print(speed)
