while True:
    number1=list(map(int,input().split()))
    if number1[0]==0: break
    number1=number1[1:]
    number1.append(-10001)
    
    number2=list(map(int,input().split()))
    number2=number2[1:]
    number2.append(-10001)
    
    m=len(number2)
    temp=set(number1)
    cross={}
    for x in number2:
        if x in temp:
            cross[x]=-float('inf')
    now=0
    for x in number1:
        if x in cross:
            cross[x]=max(cross[x],now+x)
            now=0
        else:
            now+=x
    for x in number2:
        if x in cross:
            cross[x]=max(cross[x],now+x)
            now=0
        else:
            now+=x
    answer=sum([cross[x] for x in cross])
    answer+=10001
    print(answer)
    
    
