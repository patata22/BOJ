def check(mid):
    total=0
    for i in range(n):
        for j in range(n):
            total+=min(mid,board[i][j])
    if total*2>=T:return True
    else:return False
    

n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
T=sum(sum(board[i]) for i in range(n))

l=0
r=10**13+1
while l+1<r:
    mid=(l+r)//2
    if check(mid):r=mid
    else:l=mid
if T==0:print(0)
else:print(r)
