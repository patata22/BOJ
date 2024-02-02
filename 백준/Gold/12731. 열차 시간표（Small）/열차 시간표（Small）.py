import heapq

def minute(x):
    a,b=map(int,x.split(':'))
    return 60*a+b

for tt in range(int(input())):
    t=int(input())
    A,B=map(int,input().split())
    schedule=[]
    a=[]
    b=[]
    answer=[0,0]
    for _ in range(A):
        start,end=map(minute,input().split())
        schedule.append((start,end,'A'))
    for _ in range(B):
        start,end=map(minute,input().split())
        schedule.append((start,end,'B'))
    schedule.sort()
    for start,end,station in schedule:
        if station=='A':
            if not a or a[0]>start:answer[0]+=1
            else:heapq.heappop(a)
            heapq.heappush(b, end+t)
        else:
            if not b or b[0]>start:answer[1]+=1
            else:heapq.heappop(b)
            heapq.heappush(a,end+t)
    print(f'Case #{tt+1}: {answer[0]} {answer[1]}')
    