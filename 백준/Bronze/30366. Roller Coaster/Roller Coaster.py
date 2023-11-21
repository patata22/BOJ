import sys
input=sys.stdin.readline

n,m=map(int,input().split())
group=list(map(int,input().split()))
answer=[0]*n
t=0
man=0
for i in range(n):
    if man+group[i]>m:
        t+=1
        man=group[i]
    else:
        man+=group[i]
    answer[i]=t
for x in answer:print(x)