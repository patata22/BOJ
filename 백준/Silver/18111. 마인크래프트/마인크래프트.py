import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
field=[]
for i in range(n):field+=list(map(int,input().split()))
height=max(field)
min_height=min(field)
answer_time=100000000000000
answer_height=0
while height>=min_height:
    b_temp=b
    time=0
    for x in field:
        if x==height:pass
        elif x>height:
            time+=2*(x-height)
            b_temp+=x-height
        elif x<height:
            time+=(height-x)
            b_temp-=height-x
    if b_temp>=0:
        if time<answer_time:
            answer_time=time
            answer_height=height
    height-=1

print(answer_time, answer_height)
    
