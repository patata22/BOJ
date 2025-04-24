import sys,heapq
input=sys.stdin.readline

for tt in range(int(input())):
    Q,k=map(int,input().split())
    q=[]
    result=0
    for _ in range(Q):
        cmd=input().split()
        if len(cmd)==1: print(result)
        else:
            x=int(cmd[1])
            if len(q)==k:
                if q[0]<x:
                    result^=heapq.heappop(q)
                    result^=x
                    heapq.heappush(q,x)
            else:
                heapq.heappush(q,x)
                result^=x