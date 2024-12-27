import sys
input=sys.stdin.readline

def parse(x):
    h,m=x.split(":")
    return 60*int(h)+int(m)

time=sorted([parse(input()) for _ in range(int(input()))],reverse=True)


answer=0
before=-10000
cnt=0
while time:
    now=time.pop()
    if before+20<now:
        answer+=1
        cnt=1
        before=now
    else:
        cnt+=1
        if cnt==3:
            before=-10000
print(answer)
                

