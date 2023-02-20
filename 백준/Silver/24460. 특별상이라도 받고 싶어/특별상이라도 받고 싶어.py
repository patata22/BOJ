def sol(x,y,n):
    temp=[]
    if n==1:return board[x][y]
    t=n//2
    temp.append(sol(x,y,t))
    temp.append(sol(x+t,y,t))
    temp.append(sol(x,y+t,t))
    temp.append(sol(x+t,y+t,t))
    temp.sort()
    return temp[1]

n=int(input())
board=[tuple(map(int,input().split())) for i in range(n)]
print(sol(0,0,n))
