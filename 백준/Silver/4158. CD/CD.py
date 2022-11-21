import sys
input=sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n==0 and m==0: break
    l= set()
    answer=0
    for i in range(n):
        l.add(int(input()))
    for i in range(m):
        if int(input()) in l: answer+=1
    print(answer)
