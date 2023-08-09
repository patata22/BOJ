for _ in range(int(input())):
    input()
    x,y=0,0
    for a in input():
        if a=='E':x+=1
        elif a=='W':x-=1
        elif a=='N':y+=1
        else: y-=1
    print(abs(x)+abs(y))