number=list(map(int,list(input())))
total=0
for i in range(len(number)):
    x=number[i]
    if i%2==0:
        temp = 2*x
        while temp:
            total+=temp%10
            temp//=10
    else: total+=x
print('DA') if total%10==0 else print('NE')
