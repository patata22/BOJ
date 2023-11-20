import sys
input=sys.stdin.readline
t=int(input())
l,r=2,2
answer=0
for _ in range(t):
    a,b=map(int,input().split())
    if a and a==l: answer+=1
    if b and b==r: answer+=1
    if a and a==b: answer+=1
    l,r=a,b
print(answer)