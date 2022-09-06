def checkboard(x,y):
    countw=0
    for i in range(x,x+8,2):
        for j in range(y,y+8,2):
            if lst[i][j]!='W':countw+=1
        for j in range(y+1,y+8,2):
            if lst[i][j]!='B':countw+=1
    for i in range(x+1,x+8,2):
        for j in range(y,y+8,2):
            if lst[i][j]!='B':countw+=1
        for j in range(y+1,y+8,2):
            if lst[i][j]!='W':countw+=1
    countb=0
    for i in range(x,x+8,2):
        for j in range(y,y+8,2):
            if lst[i][j]!='B':countb+=1
        for j in range(y+1,y+8,2):
            if lst[i][j]!='W':countb+=1
    for i in range(x+1,x+8,2):
        for j in range(y,y+8,2):
            if lst[i][j]!='W':countb+=1
        for j in range(y+1,y+8,2):
            if lst[i][j]!='B':countb+=1
    return(min(countw,countb))

lst=[]
answer=64
n,m=map(int,input().split())
for _ in range(n):
    lst.append(list(input()))
for i in range(n-7):
    for j in range(m-7):
        if checkboard(i,j)<answer:answer=checkboard(i,j)
print(answer)