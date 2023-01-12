for _ in range(int(input())):
    w=input()
    answer=''
    count=0
    double=0
    for i in range(97,123):
        temp = chr(i)
        c=w.count(temp)
        if c>count:
            answer=temp
            count=c
            double=0
        elif c==count:
            double=1
    if double:print('?')
    else: print(answer)
    
