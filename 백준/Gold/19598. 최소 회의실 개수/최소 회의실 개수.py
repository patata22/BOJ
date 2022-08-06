import heapq

conf=sorted([tuple(map(int,input().split())) for i in range(int(input()))])
answer=1
on=[conf[0][1]]
for start,end in conf[1:]:
    if on[0]>start: answer=max(answer,len(on)+1)
    else:heapq.heappop(on)
    heapq.heappush(on,end)

print(answer)
