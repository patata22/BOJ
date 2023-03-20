import heapq

def solution(operations):
    n=len(operations)
    minheap=[]
    maxheap=[]
    used=[0]*(n+1)
    for i in range(len(operations)):
        a,b=operations[i].split()
        b=int(b)
        if a=='I':
            heapq.heappush(minheap, (b,i))
            heapq.heappush(maxheap, (-b,i))
        elif a=='D':
            if b<0: 
                while minheap and used[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    used[heapq.heappop(minheap)[1]]=1
                    
            else:
                while maxheap and used[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    used[heapq.heappop(maxheap)[1]]=1
        
    while minheap and used[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and used[maxheap[0][1]]:
        heapq.heappop(maxheap)
    if minheap: return -maxheap[0][0], minheap[0][0]
    else: return 0,0
    