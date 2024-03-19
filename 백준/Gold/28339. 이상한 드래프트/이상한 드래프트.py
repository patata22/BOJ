import sys,heapq
input=sys.stdin.readline


def calc():
    temp=0
    for i in range(1,10):
        if not position[i]: return 0
        temp-=position[i][0][0]
    return temp

for tt in range(int(input())):
    n,k=map(int,input().split())
    player=[tuple(map(int,input().split())) for i in range(n)]
    score=0
    position=[[] for i in range(10)]
    for i in range(k):
        p,a=player[i]
        heapq.heappush(position[p], (-a,i))
    score=calc()
    l=0
    r=k-1
    while r<n-1:
        l+=1
        for i in range(1,10):
            while position[i] and position[i][0][1]<l:
                heapq.heappop(position[i])
        r+=1
        p,a=player[r]
        heapq.heappush(position[p],(-a,r))    
        score=max(score,calc())
    print(score)