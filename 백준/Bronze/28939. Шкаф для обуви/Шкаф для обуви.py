import sys
input=sys.stdin.readline

n=int(input())
k,m1,m2=map(int,input().split())
answer=0
for _ in range(n):
    number=list(map(int,input().split()))
    h=number[0]
    for x in number[2:]:
        if x*m1<h or x*m2>h*k:answer+=1
print(answer)