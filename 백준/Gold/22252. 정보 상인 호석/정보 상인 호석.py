import sys, heapq
input=sys.stdin.readline

n=int(input())
sales={}
answer=0
for _ in range(n):
    temp = input().split()
    com = int(temp[0])
    name = temp[1]
    if com ==1 and name not in sales:
        info=[]
        for x in map(int,temp[3:]):
            heapq.heappush(info, -x)
        sales[name] = info
    elif com ==1 and name in sales:
        for x in map(int, temp[3:]):
            heapq.heappush(sales[name], -x)
    elif temp[1] in sales:
        m = int(temp[2])
        info = sales[temp[1]]
        for __ in range(min(len(info),m)):
            answer -= heapq.heappop(info)
        

print(answer)
