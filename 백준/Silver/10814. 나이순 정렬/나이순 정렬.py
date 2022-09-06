import sys
input=sys.stdin.readline

member=[tuple(input().split()) for i in range(int(input()))]
member.sort(key=lambda x: int(x[0]))
for x in member:
    print(*x)
