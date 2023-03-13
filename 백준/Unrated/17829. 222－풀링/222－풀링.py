def sol(x,y,count):
    temp=[]
    if count==2:
        for i in range(2):
            for j in range(2):
                temp.append(board[x+i][y+j])
    else:
        c=count//2
        temp.append(sol(x,y,c))
        temp.append(sol(x,y+c,c))
        temp.append(sol(x+c,y,c))
        temp.append(sol(x+c,y+c,c))
    temp.sort()
    return temp[2]
    

n=int(input())

board=[tuple(map(int,input().split())) for i in range(n)]

print(sol(0,0,n))