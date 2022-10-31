wrong={}
count=0
answer=0
while True:
    x=input()
    if x=='-1':break
    a,b,c=x.split()
    a=int(a)
    if c=='right':
        count+=1
        if b in wrong:
            answer+=wrong[b]*20+a
        else: answer+=a
    else:
        if b in wrong:
            wrong[b]+=1
        else: wrong[b]=1

print(count,answer)
