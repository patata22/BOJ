import heapq,sys
input=sys.stdin.readline

for _ in range(int(input())):
    k=int(input())
    minheap=[]
    maxheap=[]
    number=[]
    deleted=[0]*k
    for i in range(k):
        command, number=input().rstrip().split()
        number=int(number)
        if command=='I':
            heapq.heappush(minheap,(number,i))
            heapq.heappush(maxheap,(-number, number,i))
        elif command=='D':
            if number==1:
                while True and maxheap:
                    temp, number, i = heapq.heappop(maxheap)
                    if not deleted[i]:
                        deleted[i]=1
                        break
            elif number==-1:
                while True and minheap:
                    number, i = heapq.heappop(minheap)
                    if not deleted[i]:
                        deleted[i]=1
                        break
                            
    maxanswer=-float('inf')
    minanswer=float('inf')
    while minheap:
        number,i=heapq.heappop(minheap)
        if not deleted[i]:
            minanswer=number
            break
    while maxheap:
        temp, number, i = heapq.heappop(maxheap)
        if not deleted[i]:
            maxanswer=number
            break
    print('EMPTY') if minanswer==float('inf') else print(maxanswer, minanswer)
                    
        
