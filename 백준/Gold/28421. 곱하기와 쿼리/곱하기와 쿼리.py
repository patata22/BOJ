import sys
input=sys.stdin.readline

def sol(b):
    for i in range(1,int(b**0.5)+1):
        if not count[i] or b%i or b//i>10000: continue
        if i==b//i:
            if count[i]>1: return 1
        else:
            if count[b//i]:return 1
    return 0
    
n,q=map(int,input().split())
number=list(map(int,input().split()))
count=[0]*10001
for x in number: count[x]+=1
for _ in range(q):
    a,b=map(int,input().split())
    if a==2:
        if number[b-1]:
            count[number[b-1]]-=1
            number[b-1]=0
            count[0]+=1
    else:
        if n==1:
            print(0)
            continue
        if b==0:
            if count[0]: print(1)
            else: print(0)
        else:print(sol(b))
