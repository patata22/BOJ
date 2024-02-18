import sys
input=sys.stdin.readline
from collections import deque
def sol():
    q=[]
    answer=[]
    q.append(a-1)
    while q:
        now=q.pop()
        answer.append(name[now])
        for to in graph[now]:
            q.append(to)
    print(''.join(answer))
        
        
n=int(input())
name=[input().rstrip() for i in range(n)]
graph=[deque() for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].appendleft(b-1)

sol()