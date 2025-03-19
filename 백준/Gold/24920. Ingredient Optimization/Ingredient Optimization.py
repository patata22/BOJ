import sys,heapq
input=sys.stdin.readline

def sol(x):
    need=U
    while delivery and delivery[-1][0]<=x:
        start,quantity,time=delivery.pop()
        heapq.heappush(q,(start+time,quantity))
    while need:
        while q and q[0][0]<x: heapq.heappop(q)
        if not q: return False
        time,quantity=heapq.heappop(q)
        if quantity>=need:
            left=quantity-need
            if left: heapq.heappush(q,(time,left))
            return True
        else: need-=quantity
        

for tt in range(int(input())):
    D,N,U=map(int,input().split())
    q=[]
    delivery=[list(map(int,input().split())) for i in range(D)]
    delivery.sort(key=lambda x: -x[0])
    order=list(map(int,input().split()))
    answer=0
    for x in order:
        result=sol(x)
        if not result: break
        answer+=1

    print(f'Case #{tt+1}: {answer}')
