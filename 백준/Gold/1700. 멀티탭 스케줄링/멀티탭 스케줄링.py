import heapq

n,k=map(int,input().split())
number=list(map(int,input().split()))
idx=[[] for i in range(k+1)]

for i in range(k):
    idx[number[i]].append(i)

for x in idx:
    x.append(float('inf'))
    x.sort(reverse=True)

number=number[::-1]

q=[]
multitap={}
answer=0

while number:
    now=number.pop()
    idx[now].pop()
    nxt=idx[now][-1]
    if now in multitap or len(multitap)<n:
        multitap[now]=nxt
        heapq.heappush(q,(-nxt,now))
    else:
        while multitap[q[0][1]]!=-q[0][0]:  heapq.heappop(q)
        answer+=1
        target=heapq.heappop(q)[1]
        multitap.pop(target)
        multitap[now]=nxt
        heapq.heappush(q,(-nxt,now))

print(answer)