import heapq,sys
input=sys.stdin.readline

n,h,t=map(int,input().split())
giant=[-int(input()) for i in range(n)]
heapq.heapify(giant)

i=0
while i<t:
    now=-heapq.heappop(giant)
    if now==1:
        heapq.heappush(giant,-now)
        break
    elif now>=h:
        i+=1
        heapq.heappush(giant,-(now//2))
    else:
        heapq.heappush(giant,-now)
        break
big=-heapq.heappop(giant)
if h>big:
    print('YES')
    print(i)
else:
    print('NO')
    print(big)

