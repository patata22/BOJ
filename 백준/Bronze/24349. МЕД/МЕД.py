n,a,b,c=map(int,input().split())
now=0
answer=0
for _ in range(n-1):
    if now==0:
        if a>b:
            now=1
            answer+=b
        else:
            now=2
            answer+=a
    elif now==1:
        if b>c:
            now=2
            answer+=c
        else:
            now=0
            answer+=b
    else:
        if a>c:
            now=1
            answer+=c
        else:
            now=0
            answer+=a
print(answer//100, answer%100)
            
