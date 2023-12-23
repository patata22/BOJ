from collections import deque
x=deque("SciComLove")
for i in range(int(input())%10):
    x.append(x.popleft())
print(''.join(x))
