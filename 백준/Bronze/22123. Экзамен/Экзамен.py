def parse(x):
    h,m,s=map(int,x.split(':'))
    return 3600*h+60*m+s
    

for _ in range(int(input())):
    s,f,k=input().split()
    s=parse(s)
    f=parse(f)
    k=int(k)*60
    if f<=s:f+=86400
    if f-s>=k: print('Perfect')
    elif f-s+3600>=k:print('Test')
    else:print('Fail')
