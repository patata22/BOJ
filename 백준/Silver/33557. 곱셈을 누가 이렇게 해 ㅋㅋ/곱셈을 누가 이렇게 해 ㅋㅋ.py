def sol():
    a,b=input().split()
    answer1=int(a)*int(b)
    temp=[]
    a=list(map(int,a))
    b=list(map(int,b))
    if len(b)>len(a):
        a,b=b,a
    while b:
        x,y=a.pop(),b.pop()
        temp.append(str(x*y))
    while a:
        temp.append(str(a.pop()))
    answer2=int(''.join(temp[::-1]))

    print(int(answer1==answer2))
    

for tt in range(int(input())):
    sol()
