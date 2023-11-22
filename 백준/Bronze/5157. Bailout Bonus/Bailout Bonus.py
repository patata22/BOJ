import sys
input=sys.stdin.readline

for _ in range(int(input())):
    if _: print()
    c,b,n,r=map(int,input().split())
    target=set(map(int,input().split()))
    answer=0
    for __ in range(n):
        a,b=map(int,input().split())
        if a in target:answer+= b*r//100
    print(f'Data Set {_+1}:\n{answer}')
    