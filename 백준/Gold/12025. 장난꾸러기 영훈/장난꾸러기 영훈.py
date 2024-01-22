number=list(map(int,input()))
count=0
for x in number:
    if x in (1,6,2,7):count+=1
k=int(input())
if 1<<count<k: print(-1)
else:
    count-=1
    k-=1
    answer=[]
    for x in number:
        if x not in (1,6,2,7):
            answer.append(x)
            continue
        else:
            if x==1 or x==6:
                if 1<<count&k: answer.append(6)
                else: answer.append(1)
            else:
                if 1<<count&k: answer.append(7)
                else:answer.append(2)
            count-=1
    print(*answer,sep='')
            
