while True:
    h1,m1,h2,m2=map(int,input().split())
    if h1==h2==m1==m2==0: break
    t1=60*h1+m1
    t2=60*h2+m2
    if t2<t1:t2+=1440
    print(t2-t1)
