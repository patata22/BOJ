for t in range(1,int(input())+1):
    number=list(map(int,input().split()))
    answer=[]
    now=number[0]
    answer.append(now-1)
    for x in number[1:]:
        answer.append(x*now)
        now-=1
    answer.pop()
    print(f'Case {t}:',*answer)
    
