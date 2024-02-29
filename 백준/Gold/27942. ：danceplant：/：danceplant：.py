dx=(-1,1,0,0)
dy=(0,0,-1,1)

def calcUp(up,down,left,right):
    if up==0: return -1
    nu = up-1
    temp=0
    for i in range(left,right+1):
        temp+=board[nu][i]
    return temp

def calcDown(up,down,left,right):
    if down==n-1: return -1
    nd = down+1
    temp=0
    for i in range(left,right+1):
        temp+=board[nd][i]
    return temp

def calcLeft(up,down,left,right):
    if left==0: return -1
    nl = left-1
    temp=0
    for i in range(up,down+1):
        temp+=board[i][nl]
    return temp

def calcRight(up,down,left,right):
    if right==n-1: return -1
    nr= right+1
    temp=0
    for i in range(up,down+1):
        temp+=board[i][nr]
    return temp

def sol():
    up=n//2-1
    down=n//2
    left=n//2-1
    right=n//2
    total=0
    direction=[]
    while 0<=up<n or 0<=down<n or 0<=left<n or 0<=right<n:
        temp=0
        d=-1
        U=calcUp(up,down,left,right)
        if U>temp:
            temp=U
            d='U'
        D=calcDown(up,down,left,right)
        if D>temp:
            temp=D
            d='D'
        L=calcLeft(up,down,left,right)
        if L>temp:
            temp=L
            d='L'
        R=calcRight(up,down,left,right)
        if R>temp:
            temp=R
            d='R'
        #print(temp,d)
        if temp<=0:
            print(total)
            print(''.join(direction))
            return
        total+=temp
        direction.append(d)
        if d=='U': up-=1
        elif d=='D':down+=1
        elif d=='L': left-=1
        elif d=='R': right+=1
        
    

n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
sol()
