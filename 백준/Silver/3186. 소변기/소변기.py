k,l,n=map(int,input().split())
used=0
stand=0
count=0
answer=[]
cmd=list(map(int,list(input())))
for i in range(1,n+1):
    x=cmd[i-1]
    if x==1:
        if not stand:
            stand=1
            count=0
        count+=1
        if count>=k: used=1
    else:
        if stand:
            stand=0
            count=0
        count+=1
        if count>=l and used:
            used=0
            answer.append(i)

if used:
    if stand: answer.append(n+l)
    else: answer.append(n+l-count)
if not answer:print('NIKAD')
else:print(*answer,sep='\n')
