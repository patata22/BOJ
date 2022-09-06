import sys
input=sys.stdin.readline

number=[int(input()) for i in range(int(input()))]
number.sort()
for x in number:print(x)