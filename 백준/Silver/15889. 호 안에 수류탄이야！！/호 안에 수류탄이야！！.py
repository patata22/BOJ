n=int(input())
if n==1: print("권병장님, 중대장님이 찾으십니다")
else:
    location = tuple(map(int,input().split()))
    distance = tuple(map(int,input().split()))
    now=location[0]+distance[0]
    for i in range(1,n-1):
        if location[i]<=now:
            now=max(now, location[i]+distance[i])
    print("권병장님, 중대장님이 찾으십니다") if now>=location[-1] else print("엄마 나 전역 늦어질 것 같아")
