def ascii(r,g,b):
    total = 2126*r+7152*g+722*b
    if total>=2040000: return '.'
    elif total>=1530000: return '-'
    elif total>=1020000: return '+'
    elif total>=510000: return 'o'
    return '#'

n,m=map(int,input().split())
board=[[] for i in range(n)]
for _ in range(n):
    temp = list(map(int,input().split()))
    for __ in range(0,3*m,3):
        board[_].append(ascii(temp[__],temp[__+1],temp[__+2]))

for _ in range(n):
    print(''.join(board[_]))
