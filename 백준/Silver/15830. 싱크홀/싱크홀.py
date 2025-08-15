v,w,d=map(int,input().split())

drop=0
answer=0
while True:
    t=w/v
    drop+=5*t*t
    if drop>=d: break
    answer+=1
    v*=0.8
print(answer)
    