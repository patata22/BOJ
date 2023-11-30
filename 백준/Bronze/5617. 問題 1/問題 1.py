count=[0]*4
while True:
    a,b,c=sorted(list(map(int,input().split())))
    if a+b<=c:
        print(*count)
        break
    count[0]+=1
    a*=a
    b*=b
    c*=c
    if a+b==c: count[1]+=1
    elif a+b>c: count[2]+=1
    else:count[3]+=1
