for t in range(1,int(input())+1):
    n,r1,c1,r2,c2 = map(int,input().split())
    x,y=abs(r1-r2),abs(c1-c2)
    answer='NO'
    if (x,y)==(1,2) or (x,y)==(2,1):answer='YES'
    print(f'Case {t}: {answer}')
