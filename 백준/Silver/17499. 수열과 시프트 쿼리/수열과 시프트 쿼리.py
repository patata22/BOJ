import sys
input=sys.stdin.readline
from collections import deque

n,q=map(int,input().split())

idx=0
number=deque(map(int,input().split()))

for _ in range(q):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        number[(idx+temp[1]-1)%n]+=temp[2]
    elif temp[0]==2:
        idx=(idx-temp[1])%n
    else: idx=(idx+temp[1])%n
answer=[]
for i in range(idx,n): answer.append(number[i])
for i in range(idx):answer.append(number[i])
print(*answer)
                                  
    
