from collections import deque

n,l,h=map(int,input().split())
score=deque(sorted(list(map(int,input().split()))))

for _ in range(l):
    score.popleft()
for _ in range(h):
    score.pop()

print(sum(score)/(n-l-h))
