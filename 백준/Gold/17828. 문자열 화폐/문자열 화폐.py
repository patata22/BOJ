n,x=map(int,input().split())
if x>26*n or n>x:print('!')
else:
    left=x-n
    money=[1]*n
    answer=[]
    for x in money:
        gap=min(left, 25)
        answer.append(chr(x+gap+64))
        left-=gap
    print(''.join(answer)[::-1])