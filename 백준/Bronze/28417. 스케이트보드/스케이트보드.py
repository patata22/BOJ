import sys
input=sys.stdin.readline

answer=0
for _ in range(int(input())):
    x=list(map(int,input().split()))
    answer=max(answer,sorted(x[:2])[1]+sum(sorted(x[2:])[3:]))
print(answer)
              