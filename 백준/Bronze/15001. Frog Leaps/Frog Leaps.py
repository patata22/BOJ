import sys
input=sys.stdin.readline

n=int(input())
now=int(input())
answer=0
for _ in range(n-1):
    x=int(input())
    answer+=(x-now)**2
    now=x
print(answer)
