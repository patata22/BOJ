y,m=map(int,input().split())
total=12*y+m
answer=0
for x in (15,9):
    temp=min(total,12)
    answer+=x*temp
    total-=temp
answer+=4*total
print(answer//12,answer%12)