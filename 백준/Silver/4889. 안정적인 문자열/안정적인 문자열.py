t=0
while True:
    t+=1
    stack=list(input())
    if stack[0]=='-':break
    answer=0
    cnt=0
    while stack:
        now=stack.pop()
        if now=='}':
            cnt+=1
        else:
            if cnt:
                cnt-=1
            else:
                answer+=1
                cnt+=1
    answer+=cnt//2
    print(f'{t}. {answer}')

