import sys
input=sys.stdin.readline

n=int(input())
number=[int(input()) for i in range(n)]
now=n
for i in range(number.index(n),-1,-1):
    if number[i]==now:
        now-=1
        n-=1
print(n)