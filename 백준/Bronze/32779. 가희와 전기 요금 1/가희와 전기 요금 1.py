import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(int(a*b*0.1056/60))
