x,y=0,0
input()
for a in input():
    if a=='N':x+=1
    elif a=='S':x-=1
    elif a=='W':y-=1
    else: y+=1
print(abs(x)+abs(y))

