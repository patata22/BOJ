def sol(depth,x,y):
    global eat
    if depth==0: return
    l=1<<(depth-1)
    total=0
    for a in (0,1):
        for b in (0,1):
            total+=getValue(depth-1,x+a*l,y+b*l)
    p,q=divmod(total%4,2)
    for a in (0,1):
        for b in (0,1):
            if a==p and b==q: eat+=getValue(depth-1,x+a*l,y+b*l)
            else: sol(depth-1,x+a*l,y+b*l)
    
def getValue(depth,x,y):
    if (depth,x,y) not in value:
        total=0
        l=1<<depth
        for i in range(x,x+l):
            for j in range(y,y+l):
                total+=board[i][j]
        value[(depth,x,y)]=total
    return value[(depth,x,y)]

for tt in range(int(input())):
    n=int(input())
    value={}
    D=-1
    temp=n
    while temp:
        D+=1
        temp//=2
    board=[list(map(int,input())) for i in range(n)]
    total=0
    for i in range(n): total+=sum(board[i])
    eat=0
    sol(D,0,0)
    print(total-eat)