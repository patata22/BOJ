import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<b and b%a==0: print(1)
    else: print(0)
