import sys,heapq
input=sys.stdin.readline

gift=[]
for _ in range(int(input())):
    x=tuple(map(int,input().split()))
    if x[0]:
        for g in x[1:]:heapq.heappush(gift,-g)
    else:
        print(-1) if not gift else print(-heapq.heappop(gift))