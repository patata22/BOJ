from collections import deque
import sys
input=sys.stdin.readline

buffer = int(input())
q=deque()
while True:
    x = int(input())
    if x==-1:
        if q:
            print(*q)
        else: print('empty')
        break
    if not x: q.popleft()
    elif len(q)<buffer: q.append(x)
