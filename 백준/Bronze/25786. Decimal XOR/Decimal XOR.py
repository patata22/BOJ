a,b=int(input()),int(input())
if a==b==0: print(0)
else:
    answer=[]
    while a or b:
        x,y=a%10,b%10
        if x<3 and y<3: answer.append(0)
        elif x>6 and y>6: answer.append(0)
        else: answer.append(9)
        a//=10
        b//=10
    print(*answer[::-1],sep='')
