import sys,heapq
input=sys.stdin.readline

def sol():
    now=0
    while works:
        end,need=heapq.heappop(works)
        if now+need>end:
            print('NO')
            return
        if extra and now+need>extra[0][0]:
            start,ee,nn = heapq.heappop(extra)
            heapq.heappush(works,(ee,nn))
            use=start-now
            heapq.heappush(works,(end,need-use))
            now+=use
        else: now+=need
        if not works and extra:
            start,ee,nn=heapq.heappop(extra)
            now=start
            heapq.heappush(works,(ee,nn))
    print('YES')
    print(now)

n=int(input())
works=[]
for _ in range(n):
    need,end=map(int,input().split())
    heapq.heappush(works, (end,need))
m=int(input())
extra=[]
for _ in range(m):
    start,need,end=map(int,input().split())
    heapq.heappush(extra,(start,end,need))

sol()
