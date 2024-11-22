from collections import deque

n=int(input())

answer=deque([n])

for i in range(1,n):
    if i%2: answer.appendleft(i)
    else: answer.append(i)


temp={}
for i in range(n):
    temp[answer[i]]=i+1

order=[temp[i] for i in range(n-1,0,-1)]
order.append(temp[n])

print('YES')
print(*answer)
print(*order)
    
