a,b,c,m=map(int,input().split())

cnt=0
tired=0
answer=0
while cnt<24:
    cnt+=1
    if tired+a>m:
        tired=max(0,tired-c)
    else:
        tired+=a
        answer+=b
print(answer)
        
