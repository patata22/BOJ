import sys
input=sys.stdin.readline

while True:
    n,m=map(int,input().split())
    if not n: break
    answer=[0]*(n+1)
    answer[m]=1
    for _ in range(n-2):answer[int(input())]=1
    for i in range(1,n+1):
        if not answer[i]:print(i)
