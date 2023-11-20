def check(y,m,d):
    if y<1989: return 'Yes'
    elif y>1989: return 'No'
    else:
        if m>2: return 'No'
        elif m==1: return 'Yes'
        else:
            if d==28: return 'No'
            else:return 'Yes'

for _ in range(int(input())):
    print(check(*map(int,input().split())))
    
