import sys
input=sys.stdin.readline

answer=0
n=int(input())
day=tuple(map(int,input().split()))

for i in range(n):
    a,b=map(int,input().split())
    if not day[i]: continue
    answer+=max(b-a,0)
print(answer)
    
