import sys
input=sys.stdin.readline

n=int(input())
answer=0
a,b=map(int,input().split())

for _ in range(n-1):
   c,d=map(int,input().split())
   answer+=a*d+b*c
   a+=c
   b+=d

print(answer)
