import sys,heapq
input=sys.stdin.readline

problem={}
minq=[]
maxq=[]

for _ in range(int(input())):
    p,l=map(int,input().split())
    heapq.heappush(minq, (l,p))
    heapq.heappush(maxq, (-l,-p))
    problem[p]=l

for _ in range(int(input())):
    temp=input().split()
    if temp[0]=='add':
        p,l=int(temp[1]), int(temp[2])
        heapq.heappush(minq, (l,p))
        heapq.heappush(maxq, (-l,-p))
        problem[p]=l
    elif temp[0]=='solved':
        p=int(temp[1])
        del problem[p]
    else:
        cmd=int(temp[1])
        if cmd==1:
            while True:
                l,p=maxq[0]
                l,p=-l,-p
                if p in problem and problem[p]==l: break
                heapq.heappop(maxq)
            print(p)  
        else:
            while True:              
                l,p=minq[0]
                if p in problem and problem[p]==l: break
                heapq.heappop(minq)
            print(p)