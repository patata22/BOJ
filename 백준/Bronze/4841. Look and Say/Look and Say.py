for _ in range(int(input())):
    number=list(input())
    answer=[]
    count=1
    now=number[0]
    for i in range(1,len(number)):
        if number[i]!=now:
            answer.append(str(count))
            answer.append(now)
            now=number[i]
            count=1
        else: count+=1
    answer.append(str(count))
    answer.append(now)
    print(''.join(answer))
