n,m=map(int,input().split())
if n*m==1:
    print(1)
    print(1)
elif n==1 or m==1:
    print(2)
    if n==1:
        answer=[]
        for i in range(m):
            if not i%2: answer.append(1)
            else: answer.append(2)
        print(*answer)
    elif m==1:
        answer=[]
        for i in range(n):
            if not i%2: answer.append(1)
            else: answer.append(2)
        print(*answer,sep='\n')
    
else:
    print(4)
    temp1=[]
    temp2=[]
    for i in range(m):
        if not i%2:
            temp1.append(1)
            temp2.append(3)
        else:
            temp1.append(2)
            temp2.append(4)
    for i in range(n):
        if not i%2: print(*temp1)
        else:print(*temp2)
