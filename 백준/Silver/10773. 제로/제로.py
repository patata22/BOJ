import sys
input=sys.stdin.readline
num=[]
for _ in range(int(input())):
    x=int(input())
    if x==0:
        num.pop()
    else: num.append(x)
print(sum(num))
