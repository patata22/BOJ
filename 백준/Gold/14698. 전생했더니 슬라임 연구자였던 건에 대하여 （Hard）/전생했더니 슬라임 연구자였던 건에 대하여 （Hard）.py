import sys,heapq
input=sys.stdin.readline

DIV=1000000007

for t in range(int(input())):
    n=int(input())
    number=list(map(int,input().split()))
    heapq.heapify(number)
    answer=1
    for i in range(n-1):
        a,b=heapq.heappop(number),heapq.heappop(number)
        temp= a*b
        answer= (answer*temp)%DIV
        heapq.heappush(number,temp)
        
    print(answer)
    
