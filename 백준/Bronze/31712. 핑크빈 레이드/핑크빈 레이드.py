c1,d1=map(int,input().split())
c2,d2=map(int,input().split())
c3,d3=map(int,input().split())
hp=int(input())
answer=0
hp-=d1+d2+d3
while hp>0:
    answer+=1
    if not answer%c1: hp-=d1
    if not answer%c2: hp-=d2
    if not answer%c3: hp-=d3

print(answer)
