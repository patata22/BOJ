import sys,heapq
input=sys.stdin.readline

def parse(x):  
    h,m,s=x.split(':')
    s,ms=s.split('.')
    return (3600*int(h)+60*int(m)+int(s))*1000+int(ms)

n=int(input())
time=sorted([tuple(map(parse,input().split())) for _ in range(n)])
q=[]
answer=0
for s,e in time:
    while q and q[0]<=s:
        heapq.heappop(q)
    heapq.heappush(q,e)
    answer=max(answer,len(q))
print(answer)