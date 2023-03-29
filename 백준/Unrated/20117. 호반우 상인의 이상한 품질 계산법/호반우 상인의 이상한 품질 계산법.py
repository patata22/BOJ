from collections import deque

n=int(input())
price=deque(sorted(list(map(int,input().split()))))
answer=0
while len(price)>1:
    answer+=price.pop()*2
    price.popleft()
if price: answer+=price[0]
print(answer)
