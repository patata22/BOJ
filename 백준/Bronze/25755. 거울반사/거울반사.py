rev={2:5,5:2, 1:1,8:8}
def parse(x):
    x=int(x)
    if x in rev: return rev[x]
    return '?'
    
cmd,n=input().split()
n=int(n)
board=[list(map(lambda x: parse(x), input().split())) for i in range(n)]
if cmd in 'LR':
    for i in range(n):
        print(*board[i][::-1])
else:
    for i in range(n-1,-1,-1):
        print(*board[i])
       