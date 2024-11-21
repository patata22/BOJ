from collections import deque

for tt in range(int(input())):
    n=int(input())
    alpha=input().split()[::-1]
    answer=deque()
    answer.append(alpha.pop())
    while alpha:
        left=ord(answer[0])
        right=ord(answer[-1])
        if ord(alpha[-1])<=left:
            answer.appendleft(alpha.pop())
        else:
            answer.append(alpha.pop())

    print(''.join(answer))
