from collections import deque

for _ in range(int(input())):
    temp=deque(input())
    n=len(temp)
    answer=[]
    answer.append(''.join(temp))
    for __ in range(n):
        temp.append(temp.popleft())
        answer.append(''.join(temp))
    answer.sort()
    print(answer[0])
    