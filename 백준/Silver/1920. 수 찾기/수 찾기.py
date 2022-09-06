import sys
input=sys.stdin.readline

input()
number=set(map(int,input().split()))
input()
for x in list(map(int,input().split())):
    print(1) if x in number else print(0)
