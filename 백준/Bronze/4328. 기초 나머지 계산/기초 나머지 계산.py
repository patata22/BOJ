def trans(n,b):
    answer=""
    while n:
        answer+=str(n%b)
        n//=b
    if not answer:return 0
    return int(answer[::-1])

while True:
    x=input()
    if x=='0':break
    b,p,m=x.split()
    b=int(b)
    p=int(p,b)
    m=int(m,b)
    print(trans(p%m,b))
