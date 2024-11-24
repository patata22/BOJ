dx=(0,1,0,-1)
dy=(1,0,-1,0)

def change(x):
    if x==' ':return '00000'
    temp = bin(ord(x)-64)[2:]
    temp= '0'*(5-len(temp))+temp
    return temp

def sol():
    temp=input()
    l=len(temp)
    idx=0
    n=""
    while temp[idx]!=' ':
        n+=temp[idx]
        idx+=1
    idx+=1
    m=""
    while temp[idx]!=' ':
        m+=temp[idx]
        idx+=1

    n=int(n)
    m=int(m)
    text=temp[idx+1:]
    board=[[0]*m for i in range(n)]
    visited=[[0]*m for i in range(n)]
    x=0
    y=0
    d=0
    for a in text:
        result=change(a)
        for b in result:
            visited[x][y]=1
            board[x][y]=b
            cnt=0
            while not (0<=x+dx[d]<n and 0<=y+dy[d]<m and not visited[x+dx[d]][y+dy[d]]):
                d=(d+1)%4
                cnt+=1
                if cnt==4: break
            x+=dx[d]
            y+=dy[d]
            
            
    for i in range(n):print(*board[i],sep='',end='')
    print()
            

for tt in range(int(input())):
    sol()
    
