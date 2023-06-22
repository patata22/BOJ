import sys
input=sys.stdin.readline

n=int(input())
if not n: print(0)
else:
    number=sorted([int(input()) for i in range(n)])
    c=round(n*0.15+0.0000000001)
    total = sum(number[c:n-c])
    print(round(total/(n-2*c)+0.00000001))
