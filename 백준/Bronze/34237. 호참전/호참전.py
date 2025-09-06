import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=[tuple(map(int,input().split())) for i in range(n)]

for _ in range(m):
    answer=0
    g,x,y=map(int,input().split())
    for a,b in number:
        if x<=a and y<=b and a+b<=g: answer+=1
    print(answer)