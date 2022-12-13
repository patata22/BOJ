import sys,heapq
input=sys.stdin.readline

n,m=map(int,input().split())

gift = list(map(lambda x: -int(x),input().split()))
child = list(map(int,input().split()))
heapq.heapify(gift)
answer=1
for need in child:
    big = -heapq.heappop(gift)
    if need>big:
        answer=0
        break
    else:
        heapq.heappush(gift, need-big)
print(answer)
