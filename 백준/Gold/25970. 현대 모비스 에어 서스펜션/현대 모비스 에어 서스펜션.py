import sys
input=sys.stdin.readline

def sol():
    target=input()
    n=len(target)

    lCnt=0
    hCnt=0

    for i in range(1,51):
        if i>n: break
        l,h=check(i,target)
        lCnt+=l
        hCnt+=h

    if lCnt>hCnt: print('HIGH', abs(lCnt-hCnt))
    elif lCnt<hCnt: print('LOW', abs(lCnt-hCnt))
    else: print('GOOD')

def check(i,target):
    l=0
    h=0
    n=len(target)
    for k in range(i,n):
        temp=target[k-i:k]
        if temp in low: l+=1
        elif temp in high: h+=1
    return l,h
    
b=int(input())
low=set()
high=set()
for _ in range(b):
    low.add(input().rstrip())
for _ in range(b):
    high.add(input().rstrip())

for _ in range(int(input())):
    sol()