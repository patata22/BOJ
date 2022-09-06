while True:
    x=list(input())
    if x==['.']:break
    temp=[]
    answer='yes'
    while x:
        now=x.pop()
        if now in (']',')'):temp.append(now)
        elif now=='(':
            if not temp or temp[-1]!=')':
                answer='no'
                break
            else:temp.pop()
            
        elif now=='[':
            if not temp or temp[-1]!=']':
                answer='no'
                break
            else:
                temp.pop()
    if temp: answer='no'
    print(answer)
