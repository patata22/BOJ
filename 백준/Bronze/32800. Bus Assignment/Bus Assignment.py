import sys
input=sys.stdin.readline

answer=0
total=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    total+=b-a
    answer=max(answer,total)
print(answer)
