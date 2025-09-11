import sys,heapq
input=sys.stdin.readline

n,k,p=map(int,input().split())

need=[int(input()) for i in range(p)]
idx=[[] for i in range(n+1)]
for i in range(len(need)):
    idx[need[i]].append(i)


for x in idx:
    x.append(float('inf'))
    x.sort(reverse=True)

need=need[::-1]
q=[]
available={}
answer=0

while need:
    now=need.pop()
    if now in available or len(available)<k:
        idx[now].pop()
        available[now]=idx[now][-1]
        heapq.heappush(q,(-idx[now][-1],now))
    else:
        while q and -q[0][0]!=available[q[0][1]]:
            heapq.heappop(q)
        answer+=1
        idx[now].pop()
        available.pop(heapq.heappop(q)[1])
        heapq.heappush(q,(-idx[now][-1],now))
        available[now]=idx[now][-1]

print(answer+k)