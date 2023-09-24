import heapq

n=int(input())
number=sorted(list(map(int,input().split())))
q=[-number.pop()]
answer=1
while number:
    now=number.pop()
    if -q[0]<=now:
        answer+=1
        heapq.heappush(q,-now)
    else:
        heapq.heappop(q)
        heapq.heappush(q,-now)

print(answer)
