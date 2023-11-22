for _ in range(int(input())):
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    if y1==y2:
        answer=0.5*(m2-m1)/(13-m1)
    else:
        answer=y2-y1-1+0.5+(m2-1)/12
    print("%.4f" %answer)
