import sys,heapq
input=sys.stdin.readline

n=int(input())
used=[0]*n
unused=0
user=[]
for _ in range(n):
    s,e=map(int,input().split())
    user.append((s,e,_))

user.sort()

q=[]
rest=[]
for i in range(n):
    s,e,idx = user[i]
    while q and q[0][0]<=s:
        heapq.heappush(rest,heapq.heappop(q)[1])
    if not rest:
        unused+=1
        heapq.heappush(q,(e,unused))
        used[idx]=unused
    else:
        num=heapq.heappop(rest)
        heapq.heappush(q,(e,num))
        used[idx]=num
answer=[0]*unused
for x in used:
    answer[x-1]+=1
print(unused)
print(*answer)
