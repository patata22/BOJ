for _ in range(int(input())):
    temp=list(input())
    n=len(temp)
    idx=0
    now=temp[0]
    count=1
    answer=[]
    for i in range(1,n):
        if temp[i]==now:
            count+=1
        else:
            answer.append(str(count))
            answer.append(now)
            now=temp[i]
            count=1
    answer.append(str(count))
    answer.append(now)
    print(' '.join(answer))
            
