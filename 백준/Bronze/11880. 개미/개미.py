import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b,c=sorted(map(int,input().split()))
    print((a+b)**2+c**2)
