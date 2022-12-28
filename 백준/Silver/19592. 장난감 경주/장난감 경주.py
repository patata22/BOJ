def binary_search():
    l=1
    r=y
    time = x/fast
    while l+1<r:
        mid = (l+r)//2
        if (x-mid)/myspeed+1<time: r=mid
        else: l=mid
    if (x-r)/myspeed+1<time: return r
    else: return -1

for _ in range(int(input())):
    n,x,y = map(int,input().split())
    speed = list(map(int,input().split()))
    myspeed = speed[-1]
    fast = max(speed)
    if myspeed==fast:print(0)
    else:
        print(binary_search())
    
