import sys
input=sys.stdin.readline

while True:
    n=int(input())
    if n==0: break
    number=list(map(int,input().split()))
    gap=float('inf')
    answer=0
    for i in range(n):
        if gap>abs(2023-number[i]):
            answer=i+1
            gap=abs(2023-number[i])
    print(answer)